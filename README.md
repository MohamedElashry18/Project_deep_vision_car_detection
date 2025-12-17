# 🚗 Driver State Detection System
**AI-based Driver Monitoring using YOLO & Streamlit**

## 📌 Overview
This project implements an intelligent **Driver State Detection System** using **Computer Vision and Deep Learning**.  
It detects unsafe driver behaviors such as:
- 😴 Drowsy / Sleeping  
- 📱 Using a mobile phone while driving  
- ✅ Normal driving state  

Users can upload **images or videos**, and the system performs **object detection** using a trained **YOLO** model.  
Results are displayed through an interactive **Streamlit** web interface.

---

## 🎯 Objectives
- Improve road safety using AI  
- Detect driver distraction and fatigue  
- Provide a simple and interactive testing interface  
- Apply object detection in a real-world scenario  

---

## 🧠 Technologies & Tools
- Python  
- YOLO (Ultralytics)  
- Streamlit  
- OpenCV  
- NumPy  
- Pillow (PIL)  

---

## 🗂️ Project Structure
```
├── app.py                 # Streamlit application
├── best.pt                # Trained YOLO model weights
├── project_car       # Model training & experiments 
└── README.md              # Project documentation
```
---
## 📦 Dataset
The dataset used in this project is hosted on **Roboflow** and is fully annotated for **YOLO Object Detection**.

🔗 Dataset URL:  
https://universe.roboflow.com/dmd-test/dm-sys-dataset/dataset/19

- Classes include:
  - Sleeping / Drowsy Driver
  - Using Mobile Phone
  - Normal Driving
- Format: YOLO (bounding boxes)
- Ready for training and inference

---

## ⚙️ How the System Works
1. Load a trained YOLO model (`best.pt`)
2. Upload a video through the Streamlit interface
3. Read the video frame-by-frame using OpenCV
4. Perform object detection on each frame
5. Draw bounding boxes for detected objects
6. If a **dangerous class** is detected:
   - Draw a **red warning circle**
   - Display the word **Dangerous**
7. Save and display the processed video with detections

---

## ▶️ Running the Application

### 1️⃣ Activate Environment
### 2️⃣ Run Streamlit App streamlit run app.py
### 3️⃣ Open in Browser http://localhost:8501
---
## 👨‍💻 Author
**Mohamed Elashry**  
Data analysis & AI 
