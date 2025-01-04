import cv2
import numpy as np

# Function to count fingers using convexity defects
def count_fingers(contour, hull):
    fingers = 0
    defects = cv2.convexityDefects(contour, hull)

    if defects is not None:
        for i in range(defects.shape[0]):
            s, e, f, d = defects[i, 0]
            start = tuple(contour[s][0])
            end = tuple(contour[e][0])
            far = tuple(contour[f][0])

            # Using cosine rule to find the angle between fingers
            a = np.linalg.norm(np.array(start) - np.array(far))
            b = np.linalg.norm(np.array(end) - np.array(far))
            c = np.linalg.norm(np.array(start) - np.array(end))
            angle = np.arccos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b)) * 57

            # Count as finger if angle is less than 90 degrees
            if angle <= 90 and d > 10000:  # d threshold filters out noise
                fingers += 1

    # Add 1 to account for the thumb (usually missed)
    return fingers + 1

# Start video capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip frame for a mirror effect
    frame = cv2.flip(frame, 1)
    roi = frame[100:400, 100:400]
    cv2.rectangle(frame, (100, 100), (400, 400), (0, 255, 0), 2)
    
    # Convert ROI to grayscale and apply blur and threshold
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (35, 35), 0)
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        max_contour = max(contours, key=cv2.contourArea)

        # Find convex hull and convexity defects
        hull = cv2.convexHull(max_contour, returnPoints=False)
        hull_points = cv2.convexHull(max_contour)
        
        # Calculate contour and hull areas
        contour_area = cv2.contourArea(max_contour)
        hull_area = cv2.contourArea(hull_points)

        # Count fingers and adjust with an offset
        fingers = count_fingers(max_contour, hull)

        # Additional logic for zero fingers (closed fist)
        if fingers == 1 and hull_area - contour_area < 1000:
            fingers = 0

        # Draw contours and hull on the original frame
        cv2.drawContours(roi, [max_contour], -1, (0, 255, 0), 2)
        cv2.drawContours(roi, [hull_points], -1, (0, 0, 255), 2)

        # Display finger count
        cv2.putText(frame, f'Fingers: {fingers}', (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)

    # Show the frame
    cv2.imshow("Finger Counter", frame)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
