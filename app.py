import streamlit as st
from ultralytics import YOLO
from PIL import Image
import io
import cv2
import tempfile
import numpy as np

st.title("Driver State Detector")

# تحميل الموديل
model = YOLO("best.pt")  # لازم يكون في نفس الفولدر

uploaded = st.file_uploader(
    "(رفع صورة أو فيديو)"     "   "  "   "  "Upload Photo OR Video ",
    type=["jpg", "jpeg", "png", "mp4", "avi", "mov"]
)

if uploaded:

    file_type = uploaded.type

    # -----------------------------------
    #          📸 معالجة الصور
    # -----------------------------------
    if file_type.startswith("image"):
        image_bytes = uploaded.read()
        img = Image.open(io.BytesIO(image_bytes))

        st.image(img, caption="Oraginal photo")

        # YOLO يحتاج ملف → نحفظ الصورة
        with open("temp.jpg", "wb") as f:
            f.write(image_bytes)

        # object detection
        results = model("temp.jpg")

        annotated = results[0].plot()  # numpy array
        st.image(annotated, caption="Result Detection")

    # -----------------------------------
    #          🎥 معالجة الفيديو
    # -----------------------------------
    elif file_type.startswith("video"):

        # حفظ الفيديو مؤقتاً
        tfile = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
        tfile.write(uploaded.read())

        st.video(tfile.name)

        st.write("... Wating Please....")

        cap = cv2.VideoCapture(tfile.name)

        frame_holder = st.empty()

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # YOLO on frame
            results = model(frame)

            # Convert frame + boxes
            annotated_frame = results[0].plot()

            # عرض الفريم
            frame_holder.image(annotated_frame, channels="BGR")

        cap.release()
        st.success("Done")
