import streamlit as st
import pandas as pd

st.set_page_config(page_title="එලවලු කඩේ", page_icon="🥕", layout="wide")
st.title("🥕 එලවලු කඩේ | මුළු ලංකාව")
st.caption("Polonnaruwa | Dambulla | Manning | Daily Update")

data = {
    "Vegetable": ["Brinjal","Tomato","Beans","Potato","Onion","Carrot","Cabbage","Chilli","Pumpkin","Cucumber"],
    "සිංහල": ["බටු","තක්කාලි","බෝංචි","අල","ලූණු","කැරට්","ගෝවා","මිරිස්","වට්ටක්කා","පිපිඤ්ඤා"],
    "Polonnaruwa": [180,160,280,200,180,200,120,450,90,80],
    "Dambulla": [145,150,120,200,170,185,60,400,80,70],
    "Manning": [200,200,160,220,200,240,80,500,110,100]
}
df = pd.DataFrame(data)

q = st.text_input("🔍 Search - batu / බටු / tomato")
if q:
    df = df[df["Vegetable"].str.lower().str.contains(q.lower()) | df["සිංහල"].str.contains(q)]

market = st.selectbox("Market එක තෝරන්න", ["All Markets","Polonnaruwa","Dambulla","Manning"])
if market == "All Markets":
    st.dataframe(df, use_container_width=True)
else:
    st.dataframe(df[["Vegetable","සිංහල",market]], use_container_width=True)

st.success("✅ Updated! මුළු ලංකාවම Live!")
