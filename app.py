import streamlit as st
import cv2
import numpy as np

file = st.file_uploader("ارفع صورة العربية من موبايلك")

if file:
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), 1)
    st.image(img, channels="BGR", caption="ERROR")
