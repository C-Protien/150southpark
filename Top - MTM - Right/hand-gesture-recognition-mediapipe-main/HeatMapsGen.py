import cv2
import mediapipe as mp
import numpy as np
import matplotlib.pyplot as plt

# Initialize MediaPipe Hands and Pose
mp_hands = mp.solutions.hands
mp_pose = mp.solutions.pose
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.85, model_complexity=1)
pose = mp_pose.Pose(min_detection_confidence=0.5)

# Initialize OpenCV
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
frame_height, frame_width, _ = frame.shape

# Create an empty heatmap
heatmap = np.zeros((frame_height, frame_width), dtype=np.uint8)

# Lists to store wrist and elbow coordinates
wrist_x_list = []
wrist_y_list = []
elbow_x_list = []
elbow_y_list = []

# Create empty heatmaps for wrist and elbow
wrist_heatmap = np.zeros((frame_height, frame_width), dtype=np.float32)
elbow_heatmap = np.zeros((frame_height, frame_width), dtype=np.float32)





while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    if not ret:
        break

    # Set the frame to a solid color (e.g. white)
    # frame.fill(255)

    # Convert the frame to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect hands and pose in the frame
    hand_results = hands.process(frame_rgb)
    pose_results = pose.process(frame_rgb)

    if hand_results.multi_hand_landmarks:

        for hand_landmarks, handedness in zip(hand_results.multi_hand_landmarks,hand_results.multi_handedness):
            if handedness.classification[0].label == 'Right':
            # Extract wrist coordinates
                wrist_x = int(hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x * frame_width)
                wrist_y = int(hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y * frame_height)

            # Draw circle on the frame at the wrist coordinates
                cv2.circle(frame, (wrist_x, wrist_y), 5, (0, 255, 0), -1)

            # Check if wrist coordinates are within frame bounds
                if 0 <= wrist_x < frame_width and 0 <= wrist_y < frame_height:
                    # Update the wrist heatmap at the wrist coordinates
                    wrist_heatmap[wrist_y, wrist_x] += 1

    if pose_results.pose_landmarks:
        # Extract elbow coordinates
        elbow_x = int(pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].x * frame_width)
        elbow_y = int(pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].y * frame_height)

        # Draw circle on the frame at the elbow coordinates
        cv2.circle(frame, (elbow_x, elbow_y), 5, (0, 255, 0), -1)

        # Check if elbow coordinates are within frame bounds
        if 0 <= elbow_x < frame_width and 0 <= elbow_y < frame_height:
            # Update the elbow heatmap at the elbow coordinates
            elbow_heatmap[elbow_y, elbow_x] += 1

    # Normalize heatmaps
    # Normalize heatmaps
    wrist_heatmap_norm = cv2.normalize(wrist_heatmap, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    elbow_heatmap_norm = cv2.normalize(elbow_heatmap, None, 64, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    # Apply color map to heatmaps
    wrist_heatmap_color = cv2.applyColorMap(wrist_heatmap_norm, cv2.COLORMAP_BONE)
    elbow_heatmap_color = cv2.applyColorMap(elbow_heatmap_norm, cv2.COLORMAP_HOT)

    # Display the frame and heatmaps
    cv2.imshow('Frame', frame)
    cv2.imshow('Wrist Heatmap', wrist_heatmap_color)
    cv2.imshow('Elbow Heatmap', elbow_heatmap_color)

    # Exit the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

# Generate and display the heatmaps using matplotlib
plt.hist2d(wrist_x_list, wrist_y_list)