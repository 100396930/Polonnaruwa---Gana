import streamlit as st
import pandas as pd
import datetime
import random

st.set_page_config(page_title="ලංකාවෙම මිල - සිංහල", page_icon="🇱🇰", layout="wide")

# --- පසුබිමෙන් ලංකාවේ ලස්සන තැන් මාරුවෙන් මාරුවට ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Sinhala:wght@400;700&display=swap');
html, body, [class*="css"] {font-family: 'Noto Sans Sinhala', sans-serif;}
.stApp {
    background: linear-gradient(rgba(0,0,0,0.62), rgba(0,0,0,0.62)), url('https://images.unsplash.com/photo-1574236170878-f4cf62143652');
    background-size: cover; background-attachment: fixed;
    animation: bgSlide 42s infinite;
}
@keyframes bgSlide {
    0% {background-image: linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0,0.55)), url('https://images.unsplash.com/photo-1574236170878-f4cf62143652');}
    14% {background-image: linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0,0.55)), url('https://images.unsplash.com/photo-1588258528574-3d43826a1e41');}
    28% {background-image: linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0,0.55)), url('https://images.unsplash.com/photo-1556740738-b6a63e27c4df');}
    42% {background-image: linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0,0.55)), url('https://images.unsplash.com/photo-1546708620-a80e488560af');}
    56% {background-image: linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0            
