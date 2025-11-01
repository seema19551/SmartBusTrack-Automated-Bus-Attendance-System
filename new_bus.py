



import cv2
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# ==============================
# GOOGLE SHEET SETUP
# ==============================
scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Bus_Attendance").sheet1

# ==============================
# QR SCANNER SETUP
# ==============================
# camera_url = "http://172.16.2.95:8080/video"

cap = cv2.VideoCapture(0)  # 0 = default laptop webcam
detector = cv2.QRCodeDetector()

print("📷 Camera started... Show QR Code to the webcam.")

# To avoid duplicate scanning within time window
last_scanned = {}
time_window = 3600  #  1 hour

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect multiple QR codes
    retval, decoded_info, points, _ = detector.detectAndDecodeMulti(frame)

    if retval:
        largest_area = 0
        selected_data = None
        selected_box = None

        # Loop through detected QR codes
        for data, bbox in zip(decoded_info, points):
            if bbox is not None and data != "":
                # Calculate area of bounding box
                x1, y1 = bbox[0]
                x2, y2 = bbox[2]
                area = abs((x2 - x1) * (y2 - y1))

                if area > largest_area:
                    largest_area = area
                    selected_data = data
                    selected_box = bbox

        # If we found a valid largest QR
        if selected_data:
            # Draw rectangle around the selected QR
            for i in range(len(selected_box)):
                pt1 = tuple(map(int, selected_box[i]))
                pt2 = tuple(map(int, selected_box[(i + 1) % len(selected_box)]))
                cv2.line(frame, pt1, pt2, (0, 255, 0), 2)

            now = datetime.now()

            # Prevent duplicates within 3 min
            if (selected_data not in last_scanned or
                (now - last_scanned[selected_data]).total_seconds() > time_window):

                print("✅ QR Code Detected:", selected_data)
                sheet.append_row([selected_data, now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S")])
                print("📌 Entry saved to Google Sheet.")

                last_scanned[selected_data] = now

    cv2.imshow("Bus QR Scanner", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
