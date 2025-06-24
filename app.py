import cv2
from deepface import DeepFace
from ultralytics import YOLO
import torch

# Load YOLOv8 model for weapon detection
weapon_model = YOLO('yolov5s.pt')  # Replace with your custom model path

# Initialize webcam
cap = cv2.VideoCapture(0)

print("[INFO] Starting surveillance...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize for better speed
    resized_frame = cv2.resize(frame, (640, 480))

    # Weapon detection
    results = weapon_model(resized_frame, verbose=False)[0]
    for box in results.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = float(box.conf[0])
        cls = int(box.cls[0])
        label = f"{weapon_model.names[cls]} {conf:.2f}"

        # Draw bounding box
        cv2.rectangle(resized_frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv2.putText(resized_frame, label, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    # Emotion Recognition (on face)
    try:
        analysis = DeepFace.analyze(resized_frame, actions=['emotion'], enforce_detection=False)
        if analysis:
            dominant_emotion = analysis[0]['dominant_emotion']
            cv2.putText(resized_frame, f"Emotion: {dominant_emotion}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)
    except Exception as e:
        print("[WARN] Face/Emotion detection error:", e)

    # Display the frame
    cv2.imshow("DRDO Surveillance Feed", resized_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
