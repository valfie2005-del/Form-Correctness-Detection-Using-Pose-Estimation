# Form-Correctness-Detection-Using-Pose-Estimation

## 📌 What the Project Does
This project is a computer vision–based system that analyses human exercise posture from video input and provides real-time corrective feedback. It focuses on evaluating bicep curl exercise form by detecting human body landmarks and calculating elbow joint angles.

Using MediaPipe Pose Estimation and OpenCV, the system determines whether the exercise posture is correct or incorrect and overlays feedback directly on the video.

---

## 🛠️ Technologies Used
- Python 3.9+
- OpenCV
- MediaPipe
- NumPy

---

## 📂 Project Structure
exercise-form-correction/
│
├── src/
│ ├── main.py
│ ├── pose_detection.py
│ ├── angle_utils.py
│ └── posture_rules.py
│
├── data/
│ └── sample_video.mp4
│
├── output/
│ └── output_video.mp4
│
├── requirements.txt
└── README.md


---

## ⚙️ How to Run the Project (Windows)

## Step 1: Install Python
Download Python from:
https://www.python.org/downloads/

✔ Make sure to select **“Add Python to PATH”** during installation.

Verify:
python --version
## Step 2: Install Required Libraries
pip install -r requirements.txt

## Step 3: Add Sample Video
Place a short exercise video inside the data folder
Rename it as:
sample_video.mp4

## Step 4: Run the Project
cd src
python main.py

🎯 Sample Output
The output demonstrates real-time posture analysis with visual feedback.

Output includes:

Human pose skeleton overlay

Elbow joint angle displayed near the arm

Text feedback indicating:

Correct bicep curl

Incomplete curl

Over-flexed arm

Processed video saved as:

output/output_video.mp4
