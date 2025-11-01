import cv2
import pandas as pd
import datetime

# Initialize camera
cap = cv2.VideoCapture(0)

detector = cv2.QRCodeDetector()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    data, bbox, _ = detector.detectAndDecode(frame)
    if data:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"QR Detected: {data} at {now}")

        # Save to CSV
        with open("bus_log.csv", "a") as f:
            f.write(f"{data},{now}\n")

    cv2.imshow("QR Scanner", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
