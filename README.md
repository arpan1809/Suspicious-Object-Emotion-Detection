# Suspicious-Object-Emotion-Detection
# 🔰 DRDO Surveillance System  
> Real-Time AI-based Weapon Detection & Emotion Recognition for Security Monitoring  
> Built with YOLOv8, DeepFace, OpenCV, and PyTorch  

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)  

---

## 🧠 Key Features  

- 🎯 Detects weapons (guns, knives, etc.) in real-time using YOLOv8  
- 😠 Classifies human emotions (angry, sad, happy, etc.) using DeepFace  
- 🖥️ Processes live webcam or CCTV feeds with OpenCV  
- 🧩 Modular, easy-to-extend Python script (plug-and-play)

## 🛠️ Tech Stack
  | Technology | Role                            |
| ---------- | ------------------------------- |
| YOLOv8     | Object detection (weapons)      |
| DeepFace   | Emotion recognition from faces  |
| OpenCV     | Real-time video feed processing |
| PyTorch    | Deep learning inference backend |


---

## 📦 Setup Instructions  

<details>  
<summary>Expand to view full setup guide</summary>  

### 🔧 Step 1: Clone the Repository  

```bash  
git clone https://github.com/arpan1809/drdo-surveillance.git  
cd drdo-surveillance

🐍 Step 2: Create & Activate a Virtual Environment (Optional
# Create virtual environment  
python -m venv venv  

# Activate it  
# Windows:  
venv\Scripts\activate  

📦 Step 3: Install Dependencies
pip install ultralytics deepface opencv-python-headless

# macOS/Linux:  
source venv/bin/activate

🧠 Step 4: Add YOLOv8 Weapon Detection Model
Download or train a best.pt model to detect weapons (via Roboflow or GitHub).

Place best.pt in the root folder like this:

text
drdo-surveillance/  
├── best.pt  
├── drdo_surveillance.py


▶️ Step 5: Run the Surveillance System
bash
python drdo_surveillance.py  
Ensure your webcam is connected.
Press q to exit the stream.

