    import streamlit as st
import pandas as pd
import streamlit as st
import pandas as pd

st.set_page_config(page_title="එලවලු කඩේ SUPER", page_icon="🥕", layout="wide")
st.title("🥕 SUPER එලවලු කඩේ")
st.caption("Polonnaruwa | Dambulla | Manning")

data = {
    "Vegetable": ["Brinjal","Tomato","Beans","Potato","Onion","Carrot","Cabbage","Chilli"],
    "සිංහල": ["බටු","තක්කාලි","බෝංචි","අල","ලූණු","කැරට්","ගෝවා","මිරිස්"],
    "Polonnaruwa": [180,160,280,200,180,200,120,450],
    "Dambulla": [145,150,120,200,170,185,60,400],
    "Manning": [200,200,160,220,200,240,80,500],
    "Icon": ["🍆","🍅","🫘","🥔","🧅","🥕","🥬","🌶️"]
}
df = pd.DataFrame(data)

q = st.text_input("🔍 Search - batu / බටු")
if q:
    df = df[df["Vegetable"].str.lower().str.contains(q.lower()) | df["සිංහල"].str.contains(q)]

tab1, tab2 = st.tabs(["📋 Prices", "💰 Profit"])
with tab1:
    st.dataframe(df, use_container_width=True)
    st.bar_chart(df.set_index("Vegetable")[["Polonnaruwa","Dambulla","Manning"]])
with tab2:
    buy = st.number_input("Bought Price", 100)
    sell = st.number_input("Selling Price", 150)
    qty = st.number_input("Kg", 10)
    st.success(f"Profit: Rs. {(sell-buy)*qty}")

st.success("✅ App Working!")
st.title("🥕 එලවලු කඩේ")
st.write("Polonnaruwa | Dambulla | Manning")

data = {
    "Vegetable": ["Brinjal","Tomato","Beans","Potato","Onion"],
    "සිංහල": ["බටු","තක්කාලි","බෝංචි","අල","ලූණු"],
    "Polonnaruwa": [180,160,280,200,180],
    "Dambulla": [145,150,120,200,170],
    "Manning": [200,200,160,220,200]
}
df = pd.DataFrame(data)

search = st.text_input("Search")
if search:
    df = df[df["Vegetable"].str.lower().str.contains(search.lower())]

st.dataframe(df)
st.bar_chart(df.set_index("Vegetable")[["Polonnaruwa","Dambulla","Manning"]])

st.success("App Working!")
