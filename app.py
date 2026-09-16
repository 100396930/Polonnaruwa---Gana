import streamlit as st
import pandas as pd

st.set_page_config(page_title="Elavalu Kade", page_icon="🥕")
st.title("🥕 Elavalu Kade")
st.write("Polonnaruwa | Dambulla | Manning")

data = {
"Vegetable": ["Brinjal", "Tomato", "Beans", "Potato", "Onion"],
"Sinhala": ["Batu", "Thakkali", "Bonchi", "Ala", "Lunu"],
"Polonnaruwa": [180, 160, 280, 200, 180],
"Dambulla": [145, 150, 120, 200, 170],
"Manning": [200, 200, 160, 220, 200]
}
df = pd.DataFrame(data)

search = st.text_input("Search batu")
if search:
    df = df[df["Vegetable"].str.lower().str.contains(search.lower())]

st.dataframe(df, use_container_width=True)
st.bar_chart(df.set_index("Vegetable")[["Polonnaruwa", "Dambulla", "Manning"]])
st.success("App Working!")      
