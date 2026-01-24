DeepTrack – Real-Time Face Recognition Attendance System 🎯

📌 Overview

DeepTrack is a real-time face recognition–based attendance system that detects and recognizes faces from live video streams. It uses deep learning models to automatically mark attendance and send confirmation emails to students, reducing manual effort and errors.

The system integrates **YOLOv8** for fast face detection and **DeepFace** for accurate face recognition using facial embeddings and similarity thresholds.

🚀 Features

* Real-time face detection using webcam or video input
* Accurate face recognition using deep learning embeddings
* Automatic attendance marking
* 📧 Attendance confirmation emails sent to students
* Supports multiple face detection in a single frame
* Scalable and modular project structure

🛠️ Tech Stack

* **Programming Language:** Python
* **Face Detection:** YOLOv8
* **Face Recognition:** DeepFace
* **Computer Vision:** OpenCV
* **Deep Learning Frameworks:** TensorFlow / PyTorch
* **Email Service:** SMTP (Python email libraries)
* **Data Handling:** NumPy, Pandas

📂 Project Structure

DeepTrack/
│── core1/
│   ├── face_detection.py
│   ├── face_recognition.py
│   ├── embeddings/
│── data/
│   ├── known_faces/
│   ├── attendance.csv
│── utils/
│── email_service.py
│── requirements.txt
│── main.py
│── README.md


⚙️ How It Works

1. Capture live video input using a webcam
2. Detect faces in each frame using YOLOv8
3. Extract facial embeddings using DeepFace
4. Compare embeddings with stored data using a threshold
5. Mark attendance automatically on successful match
6. 📧 Send attendance confirmation email to the registered student

📧 Email Notification System

* Sends automatic attendance confirmation emails to students
* Emails are triggered only after successful face recognition
* Ensures transparency and real-time updates
* Can be configured for institutional SMTP servers


▶️ Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/your-username/DeepTrack.git
cd DeepTrack

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run the Project

python main.py

📊 Attendance Output

* Attendance records are stored in a CSV file
* Each student is marked only once per session
* Email confirmation is sent immediately after marking attendance

💡 Use Cases

* College and school attendance systems
* Office employee attendance
* Secure access control systems
* Smart surveillance and monitoring systems

🔮 Future Enhancements

* Web-based attendance dashboard
* Cloud database integration
* Face mask detection support
* Mobile application integration
* SMS and WhatsApp notification support

👩‍💻 Author

**Shreeja PN**
Integrated M.Tech – Software Engineering
VIT Vellore

