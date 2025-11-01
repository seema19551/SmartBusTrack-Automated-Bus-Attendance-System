# SmartBusTrack-Automated-Bus-Attendance-System

### 🚀 Overview
SmartBusTrack is a **QR code-based bus attendance system** that automatically records bus entry and exit using a **camera feed** and stores the data in **Google Sheets** in real time.  
It eliminates manual checking and provides a **low-cost, accurate, and scalable** solution for schools, colleges, and transport companies.

---

### 🧠 Features
- Detects and reads QR codes through webcam or CCTV feed  
- Logs bus number, date, and time automatically to Google Sheets  
- Prevents duplicate scans within a time window (e.g., 1 hour)  
- Works on both **Laptop** and **Raspberry Pi**  
- Cloud-based attendance record — accessible anywhere  

---

### ⚙️ Tech Stack
- **Python**  
- **OpenCV** – For QR detection  
- **Google Sheets API** – For cloud logging  
- **Raspberry Pi / Laptop** – For deployment  

---

### 🖥️ Setup Instructions
1. Clone this repository  
   ```bash
   git clone https://github.com/seema19551/SmartBusTrack.git
   cd SmartBusTrack

Install dependencies
   ```bash
pip install opencv-python gspread oauth2client 




