# Hand Gesture Finger Counting using OpenCV

This project uses OpenCV to count the number of fingers shown in a hand gesture captured by a webcam. The program processes the video feed, detects contours and convexity defects, and uses the cosine rule to count the number of visible fingers. It displays the count on the screen in real-time.

## A demonstration
This video demonstrates how the code works by showing the process of counting fingers using OpenCV. It visualizes the key steps in action, including detecting and counting fingers in real-time.

[Click here to view the video](https://raw.githubusercontent.com/Bugates/Finger_count_using_OpenCV/refs/heads/main/Number%20of%20fingers.mp4)

## Features
- Real-time finger counting using webcam feed.
- Uses convexity defects and the cosine rule to determine the number of fingers.
- Includes noise filtering to improve detection accuracy.
- Displays the count on the screen, updating live.
- Detects a closed fist (0 fingers) when no visible fingers are shown.

## Requirements
- Python 3.x
- OpenCV (`cv2` library)
- NumPy

To install the necessary libraries, use:
```bash
pip install opencv-python numpy
```

## How to Use

1. Clone the repository:
    ```bash
    git clone https://github.com/Bugates/Finger_count_using_OpenCV.git
    ```

2. Run the Python script:
    ```bash
    python finger_counter.py
    ```

3. The program will open the webcam, and you will see the live video feed with the number of fingers detected displayed on the screen.

4. Press `q` to exit the application.

## How It Works

- The script captures video from the webcam using OpenCV.
- A region of interest (ROI) is selected for processing the hand gesture.
- The hand is detected by converting the frame to grayscale, applying Gaussian blur, and thresholding.
- Convexity defects are used to identify the fingers by analyzing the contour of the hand.
- The number of fingers is determined based on the angle between convex defects, with a threshold to filter noise.
- The final count is displayed on the screen.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Acknowledgements

- OpenCV for the image processing tools.
- NumPy for numerical operations.
