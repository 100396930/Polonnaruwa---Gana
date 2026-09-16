import streamlit as st
st.set_page_config(page_title="Polonnaruwa Gana", page_icon="🌾")
st.title("🌾 පොළොන්නරුව මිල")
st.caption("කදුරුවෙල / දඹුල්ල ඇත්ත මිල")
prices = {"තක්කාලි 1kg": 330,"කැරට් 1kg": 185,"වට්ටක්කා 1kg": 175,"ගෝවා 1kg": 250,"රතුළූණු 1kg": 320,"හාල් නාඩු 1kg": 230,"පොල් 1ක්": 140,"පරිප්පු 1kg": 295,}
item = st.selectbox("බඩුව තෝරන්න", list(prices.keys()))
shop_price = st.number_input("කඩේ ගාන Rs.", value=0)
if st.button("Check කරන්න", type="primary"):
    fair = prices[item]
    if shop_price == 0:
        st.warning("ගාන දාන්න")
    elif shop_price <= fair + 30:
        st.success(f"✅ සාධාරණයි. ඇත්ත මිල Rs.{fair}")
        st.balloons()
    else:
        st.error(f"🚨 වැඩියි! ඇත්ත මිල Rs.{fair}යි. වැඩිපුර Rs.{shop_price - fair}")
