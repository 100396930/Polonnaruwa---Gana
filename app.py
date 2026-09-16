import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="එලවලු කඩේ SUPER", page_icon="🥕", layout="wide")
st.title("🥕 SUPER එලවලු කඩේ - මුළු ලංකාව")
st.caption("Polonnaruwa | Dambulla | Manning | Live + Graph + Profit")

# Data
data = {
    "Vegetable": ["Brinjal","Tomato","Beans","Potato","Onion","Carrot","Cabbage","Chilli","Pumpkin","Cucumber"],
    "සිංහල": ["බටු","තක්කාලි","බෝංචි","අල","ලූණු","කැරට්","ගෝවා","මිරිස්","වට්ටක්කා","පිපිඤ්ඤා"],
    "Polonnaruwa": [180,160,280,200,180,200,120,450,90,80],
    "Dambulla": [145,150,120,200,170,185,60,400,80,70],
    "Manning": [200,200,160,220,200,240,80,500,110,100],
    "Image": ["🍆","🍅","🫘","🥔","🧅","🥕","🥬","🌶️","🎃","🥒"]
}
df = pd.DataFrame(data)

# Search
q = st.text_input("🔍 Search - batu / බටු / tomato")
if q:
    df = df[df["Vegetable"].str.lower().str.contains(q.lower()) | df["සිංහල"].str.contains(q)]

# Tabs
tab1, tab2, tab3 = st.tabs(["📋 Prices", "📈 Graph", "💰 Profit"])

with tab1:
    market = st.selectbox("Market", ["All","Polonnaruwa","Dambulla","Manning"])
    if market == "All":
        st.dataframe(df, use_container_width=True)
    else:
        st.dataframe(df[["Image","Vegetable","සිංහල",market]], use_container_width=True)
    st.map(pd.DataFrame({"lat":[7.94,7.87,6.93],"lon":[81.00,80.65,79.86]}))

with tab2:
    fig = px.bar(df, x="Vegetable", y=["Polonnaruwa","Dambulla","Manning"], barmode="group", title="Price Comparison")
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    veg = st.selectbox("Vegetable", df["Vegetable"])
    buy = st.number_input("Bought Price", 100)
    sell = st.number_input("Selling Price", 150)
    qty = st.number_input("Kg", 10)
    profit = (sell - buy) * qty
    st.metric("Profit", f"Rs. {profit}")

st.success("✅ SUPER APP LIVE! - කවදාවත් නැති එකක්!")
