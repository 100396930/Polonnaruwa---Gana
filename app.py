import streamlit as st
import pandas as pd

st.title("Polonnaruwa Gana Price")

# Data load - CSV එකක් තියෙනවා නම් ඒක load වෙනවා
try:
    df = pd.read_csv("prices.csv")
except:
    df = pd.DataFrame({
        'Vegetable': ['brinjal', 'tomato', 'beans', 'leeks', 'carrot', 'cabbage', 'pumpkin', 'cucumber', 'okra', 'potato', 'onion', 'beetroot', 'chilli', 'dhal'],
        'Price': [200, 150, 300, 250, 180, 120, 100, 80, 220, 200, 180, 250, 400, 350]
    })

# Search - No emoji
search_query = st.text_input("Search", "")

# Lankawe elawalu map - batu, wambatu okkoma
sinhala_map = {
    "batu": "brinjal", "wambatu": "brinjal", "brinjal": "brinjal",
    "thakkali": "tomato", "tomato": "tomato",
    "bonchi": "beans", "mae": "long beans",
    "leeks": "leeks", "carrot": "carrot", "gowwa": "cabbage",
    "wattakka": "pumpkin", "kekiri": "cucumber",
    "pathola": "snake gourd", "wetakolu": "luffa",
    "bandakka": "okra", "dambala": "winged bean",
    "karawila": "bitter gourd", "murunga": "drumstick",
    "capsicum": "capsicum", "miris": "chilli", "maalu miris": "capsicum",
    "ala": "potato", "bathala": "sweet potato", "manyokka": "manioc",
    "lunu": "onion", "sudu lunu": "garlic",
    "beetroot": "beetroot", "rabu": "radish",
    "mukunuwenna": "mukunuwenna", "gotukola": "gotukola",
    "kankun": "kangkung", "nivithi": "spinach", "salada": "lettuce",
    "parippu": "dhal", "mung": "green gram"
}

if search_query:
    q = search_query.lower().strip()
    q = sinhala_map.get(q, q)
    for k, v in sinhala_map.items():
        if k in q:
            q = v
            break
    filtered_df = df[df['Vegetable'].str.lower().str.contains(q, na=False)]
else:
    filtered_df = df

st.dataframe(filtered_df)
st.write(f"Total: {len(filtered_df)} items") 
