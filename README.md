# 💡 AI Emergency Decision Support System

An **AI-driven emergency decision support system** designed for **post-surgery cardiac patients**.  
The system continuously monitors vital signs, detects **bradycardia**, and assists doctors in **fast decision-making** for Atropine injection — reducing emergency response time.

---

## 🧠 Inspiration
This project was inspired by a real incident where a cardiac patient developed sudden **bradycardia** after surgery, and the delay in giving Atropine caused critical risk.  
Our system aims to use **AI alerts** and a **future microfluidic patch** to reduce that delay and save lives.

---

## ⚙️ Features
- Monitors simulated **Heart Rate (HR)** and **Blood Pressure (BP)**.  
- Detects **abnormal HR (<80 bpm)**.  
- Sends **emergency alerts** to the doctor.  
- Doctor approves (Yes/No) for Atropine injection.  
- Logs all actions automatically in `patient_log.csv`.  
- Future enhancement: **microfluidic patch** to release Atropine automatically.

---

## 🩺 Technologies Used
- **Python 3**  
- Built-in libraries: `random`, `time`, `csv`, `datetime`  
- No external dependencies (see `requirements.txt`).

---

## 🧩 How to Run
1. Clone or download this repository:
   ```bash
   git clone https://github.com/kavyapriya-bt/AI-Emergency-detection-support.git
   cd AI-Emergency-detection-support
