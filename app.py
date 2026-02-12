import streamlit as st
from streamlit_webrtc import webrtc_streamer
import cv2
import mediapipe as mp
# إضافة هذا السطر لحل مشكلة الـ AttributeError
import mediapipe.python.solutions.hands as mp_hands
import mediapipe.python.solutions.drawing_utils as mp_draw
import av

st.title("Hand Tracking Live 🖐️")

# إعداد النموذج بالطريقة الجديدة
hands = mp_hands.Hands(
    static_image_mode=False, 
    max_num_hands=2, 
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

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

webrtc_streamer(key="hand-tracking", video_frame_callback=video_frame_callback)
