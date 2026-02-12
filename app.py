import streamlit as st
from streamlit_webrtc import webrtc_streamer
import cv2
import av

st.title("تجربة الكاميرا البسيطة 📸")
st.write("لو شفت صورتك أبيض وإسود، يبقى إنت كدة برمجت أول تطبيق رؤية حاسوبية!")

def video_frame_callback(frame):
    # تحويل الفريم لمصفوفة بكسلات
    img = frame.to_ndarray(format="bgr24")
    
    # تحويل الصورة لأبيض وإسود (Gray)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # نرجع الصورة بعد التعديل عشان تتعرض في الموقع
    return av.VideoFrame.from_ndarray(gray_img, format="gray")

# سطر واحد بيشغل الكاميرا في المتصفح
webrtc_streamer(key="simple-camera", video_frame_callback=video_frame_callback)
