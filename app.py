    import streamlit as st
import pandas as pd

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
