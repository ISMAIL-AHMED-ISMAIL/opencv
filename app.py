import streamlit as st
from streamlit_webrtc import webrtc_streamer
import cv2
import mediapipe as mp
import av

# إعدادات MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

st.title("Hand Tracking Live 🖐️")

def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    
    # تحويل الصورة لمعالجتها
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    # رسم النقاط على اليد
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    return av.VideoFrame.from_ndarray(img, format="bgr24")

# تشغيل الكاميرا في المتصفح
webrtc_streamer(key="hand-tracking", video_frame_callback=video_frame_callback)
