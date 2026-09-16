# # ලංකාවේ හැම එළවළුවම - FULL LIST - No Error
search_query = st.text_input("Search", "")
sinhala_map = {
    "බටු": "brinjal", "වම්බටු": "brinjal", "batu": "brinjal",
    "තක්කාලි": "tomato", "thakkali": "tomato",
    "බෝංචි": "beans", "bonchi": "beans",
    "මෑකරල්": "long beans", "mae": "long beans",
    "ලීක්ස්": "leeks", "leeks": "leeks",
    "කැරට්": "carrot", "ගෝවා": "cabbage",
    "වට්ටක්කා": "pumpkin", "wattakka": "pumpkin",
    "කැකිරි": "cucumber", "පතෝල": "snake gourd",
    "වැටකොළු": "luffa", "බණ්ඩක්කා": "okra", "bandakka": "okra",
    "දඹල": "winged bean", "කරවිල": "bitter gourd",
    "මුරුංගා": "drumstick", "මාළු මිරිස්": "capsicum",
    "මිරිස්": "chilli", "miris": "chilli",
    "අල": "potato", "බතල": "sweet potato",
    "මඤ්ඤොක්කා": "manioc", "ලූනු": "onion", "lunu": "onion",
    "සුදු ලූනු": "garlic", "බීට්රූට්": "beetroot",
    "රාබු": "radish", "මුකුණුවැන්න": "mukunuwenna",
    "ගොටුකොළ": "gotukola", "කංකුං": "kangkung",
    "නිවිති": "spinach", "සලාද": "lettuce", "කොහිල": "kohila",
    "පරිප්පු": "dhal", "මුං": "green gram", "කඩල": "chickpea"
}

if search_query:
    q = search_query.lower().strip()
    q = sinhala_map.get(q, q)
    # batu වගේ ඇතුලත් නම්
    for k, v in sinhala_map.items():
        if k in q:
            q = v
               q = sinhala_map.get(q, q)
    for k, v in sinhala_map.items():
        if k in q:
            q = v
            break
    filtered_df = df[df['Vegetable'].str.lower().str.contains(q, na=False)]
else:
    filtered_df = df

st.dataframe(filtered_df) 
    
