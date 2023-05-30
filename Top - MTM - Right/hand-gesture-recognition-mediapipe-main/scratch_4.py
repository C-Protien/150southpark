
import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5, max_num_hands=2)

# Set up Webcam
cap = cv2.VideoCapture(0)

# Initialize Mediapipe drawing module
mp_drawing = mp.solutions.drawing_utils

while True:
    # Read Webcam Frame
    success, img = cap.read()
    if not success:
        break

    # Convert Image to RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Detect Hands
    results = hands.process(img_rgb)

    # Draw Landmarks on Hands
    if results.multi_hand_landmarks:
        for hand_handedness, hand_landmarks in zip(results.multi_handedness ,results.multi_hand_landmarks):
            # if hand_handedness.classification[0].label == 'Right':
             mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Display Output Image
    cv2.imshow("Hand Landmark Detection", img)

    # Exit on Escape Key Press
    if cv2.waitKey(1) == 27:
        break

# Clean Up
cap.release()
cv2.destroyAllWindows()