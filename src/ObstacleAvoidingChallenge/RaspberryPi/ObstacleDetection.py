import cv2
import numpy as np
import serial
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

button_pin = 23
button = False

GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)



# Function to calculate control points for a quadratic Bézier curve
def calculate_control_points(start, end, curvature=0.5):
    mid_x = (start[0] + end[0]) // 2
    mid_y = (start[1] + end[1]) // 2

    # Calculate direct ion vector
    dx = end[0] - start[0]
    dy = end[1] - start[1]

    # Calculate perpendicular vector (for curvature)
    perp_x = -dy
    perp_y = dx

    # Normalize and scale by curvature
    length = np.sqrt(perp_x ** 2 + perp_y ** 2)
    if length > 0:
        perp_x = perp_x / length * curvature * 100
        perp_y = perp_y / length * curvature * 100

    # Control point is the midpoint offset by the perpendicular vector
    control_x = mid_x + perp_x
    control_y = mid_y + perp_y

    return (int(control_x), int(control_y))


# Function to draw a Bézier curve
def draw_bezier_curve(img, start, control, end, color, thickness=3, num_points=50):
    points = []
    for i in range(num_points + 1):
        t = i / num_points
        # Quadratic Bézier formula
        x = (1 - t) ** 2 * start[0] + 2 * (1 - t) * t * control[0] + t ** 2 * end[0]
        y = (1 - t) ** 2 * start[1] + 2 * (1 - t) * t * control[1] + t ** 2 * end[1]
        points.append((int(x), int(y)))

    # Draw the curve as connected line segments
    for i in range(len(points) - 1):
        cv2.line(img, points[i], points[i + 1], color, thickness)


cap = cv2.VideoCapture("track_test_video.mp4")  # replace with your file name
ser = serial.Serial('/dev/serial0', 9600, timeout=1)
ser.write(b"test\n")
print(ser.readline())

# Path planning variables
path_points = []  # Store points for the path
max_path_points = 5  # Maximum number of points to keep in the path

while True:

    button_state = GPIO.input(button_pin)

    if button_state == GPIO.LOW:  # If using PUD_UP, button pressed means LOW
        print("Button Pressed!")
        time.sleep(0.2)  # Debounce delay
        button = True
        ser.write(b"START\n")

    time.sleep(0.1)  # Small delay to prevent busy-waiting


    while button:
        ret, frame = cap.read()
        if not ret:
            break

        h, w, _ = frame.shape
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # HSV ranges
        lower_red1, upper_red1 = np.array([0, 120, 70]), np.array([10, 255, 255])
        lower_red2, upper_red2 = np.array([170, 120, 70]), np.array([180, 255, 255])
        lower_green, upper_green = np.array([40, 70, 70]), np.array([90, 255, 255])

        # Masks
        mask_red = cv2.inRange(hsv, lower_red1, upper_red1) | cv2.inRange(hsv, lower_red2, upper_red2)
        mask_green = cv2.inRange(hsv, lower_green, upper_green)

        # Contours
        contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours_green, _ = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Yellow path window
        path_width = 400
        path_window = (w // 2 - path_width // 2, 0, w // 2 + path_width // 2, h)
        cv2.rectangle(frame, (path_window[0], path_window[1]),
                      (path_window[2], path_window[3]),
                      (0, 255, 255), 2)

        decision = "None"
        candidates = []
        bottom_center = (w // 2, h)

        # RED blocks
        for cnt in contours_red:
            if cv2.contourArea(cnt) > 500:
                x, y, bw, bh = cv2.boundingRect(cnt)
                cx, cy = x + bw // 2, y + bh // 2

                # Draw red bounding box
                cv2.rectangle(frame, (x, y), (x + bw, y + bh), (0, 0, 255), 2)
                # Draw line from bottom center to block center
                cv2.line(frame, bottom_center, (cx, cy), (0, 0, 255), 2)

                # Candidate only if inside yellow ROI
                if path_window[0] < cx < path_window[2]:
                    print("Block detected in car's path")
                    candidates.append(("RED", (x, y, bw, bh), bw * bh))

        # GREEN blocks
        for cnt in contours_green:
            if cv2.contourArea(cnt) > 500:
                x, y, bw, bh = cv2.boundingRect(cnt)
                cx, cy = x + bw // 2, y + bh // 2

                # Draw green bounding box
                cv2.rectangle(frame, (x, y), (x + bw, y + bh), (0, 255, 0), 2)
                # Draw line from bottom center to block center
                cv2.line(frame, bottom_center, (cx, cy), (0, 255, 0), 2)

                # Candidate only if inside yellow ROI
                if path_window[0] < cx < path_window[2]:
                    print("Block detected in car's path")
                    candidates.append(("GREEN", (x, y, bw, bh), bw * bh))

        # Choose smallest box in ROI
        current_obstacle = None
        if candidates:
            candidates.sort(key=lambda c: c[2])  # sort by area
            color, (x, y, bw, bh), area = candidates[0]

            if color == "RED":
                decision = "RIGHT"
            elif color == "GREEN":
                decision = "LEFT"

            # Store obstacle information for path planning
            current_obstacle = (x + bw // 2, y + bh // 2, color, bw, bh)

            # Highlight chosen smallest box in yellow
            cv2.rectangle(frame, (x, y), (x + bw, y + bh), (0, 255, 255), 3)
            cv2.line(frame, bottom_center, (x + bw // 2, y + bh // 2), (0, 255, 255), 3)

        # PATH PLANNING - Create smooth blue path
        if current_obstacle:
            # Calculate avoidance point based on block position and type
            obstacle_x, obstacle_y, color, bw, bh = current_obstacle

            # Determine avoidance direction (left for red, right for green)
            if color == "RED":  # Go right
                avoidance_x = obstacle_x + bw * 2
            else:  # GREEN - Go left
                avoidance_x = obstacle_x - bw * 2

            avoidance_y = obstacle_y - bh * 2

            # Add the avoidance point to our path
            path_points.append((avoidance_x, avoidance_y))

            # Keep only the most recent points
            if len(path_points) > max_path_points:
                path_points.pop(0)

        # Draw the smooth path if we have enough points
        if len(path_points) >= 2:
            # Start from the bottom center of the frame
            start_point = bottom_center

            # Draw the path as a series of Bézier curves
            for i in range(len(path_points) - 1):
                control_point = calculate_control_points(
                    start_point if i == 0 else path_points[i - 1],
                    path_points[i]
                )
                draw_bezier_curve(
                    frame,
                    start_point if i == 0 else path_points[i - 1],
                    control_point,
                    path_points[i],
                    (255, 0, 0),  # Blue color
                    5  # Thickness
                )

            # Draw the final segment to the last point
            if len(path_points) > 1:
                control_point = calculate_control_points(
                    path_points[-2],
                    path_points[-1]
                )
                draw_bezier_curve(
                    frame,
                    path_points[-2],
                    control_point,
                    path_points[-1],
                    (255, 0, 0),  # Blue color
                    5  # Thickness
                )

        # Draw path points for visualization (optional)
        for point in path_points:
            cv2.circle(frame, (int(point[0]), int(point[1])), 8, (255, 255, 0), -1)

        # Show decision
        ser.write(f"{decision}\n")
        print(ser.readline())
        cv2.putText(frame, decision, (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (255, 255, 255), 2)

        cv2.imshow("Frame", frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
