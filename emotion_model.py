import cv2
from fer import FER

def detect_emotion():
    try:
        detector = FER(mtcnn=True)

        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        if not cap.isOpened():
            return "neutral"

        detected_emotion = "neutral"

        while True:
            ret, frame = cap.read()

            if not ret or frame is None:
                continue   # skip bad frames

            frame = cv2.flip(frame, 1)

            # detect safely
            try:
                result = detector.detect_emotions(frame)
            except:
                result = []

            if result:
                emotions = result[0]["emotions"]
                detected_emotion = max(emotions, key=emotions.get)

            cv2.putText(frame, f"Live: {detected_emotion}", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)

            cv2.putText(frame, "Press Q to Capture", (20, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)

            cv2.imshow("AI Emotion Detection", frame)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

        return detected_emotion

    except Exception as e:
        print("ERROR:", e)
        return "neutral"


if __name__ == "__main__":
    detect_emotion()