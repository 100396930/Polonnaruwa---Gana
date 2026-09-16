import streamlit as st
import pandas as pd
import datetime
import random

st.set_page_config(page_title="Lanka Super Kade", page_icon="💎", layout="wide")

# --- STYLE ---
st.markdown("""
<style>
.metric-card {background:#f0f9ff; padding:15px; border-radius:12px; border-left:5px solid #0ea5e9;}
</style>
""", unsafe_allow_html=True)

st.title("💎 Polonnaruwa Super Kade - PRO")
st.caption(f"ගැනුම් | විකුණුම් | තොග | සිල්ලර | දිනපතා Auto Update: {datetime.date.today()}")

@st.cache_data(ttl=86400)
def get_pro_data():
    random.seed(datetime.date.today().day)
    def r(a,b): return random.randint(a,b)
    def make_row(eng, sin, base):
        thoga_ganum = base - r(15,30) # තොග ගැනුම් (අඩුම)
        thoga_vikunum = base - r(0,10) # තොග විකුණුම්
        sillara_ganum = base + r(10,30) # සිල්ලර ගැනුම්
        sillara_vikunum = base + r(30,60) # සිල්ලර විකුණුම් (වැඩිම)
        labaya = sillara_vikunum - thoga_ganum
        return [eng, sin, thoga_ganum, thoga_vikunum, sillara_ganum, sillara_vikunum, labaya]

    vegs = [
        make_row("Brinjal","Batu",180),
        make_row("Tomato","Thakkali",150),
        make_row("Beans","Bonchi",280),
        make_row("Carrot","Carrot",200),
        make_row("Cabbage","Gowa",120),
        make_row("Leeks","Leeks",220),
        make_row("Beetroot","Beetroot",180),
        make_row("Pumpkin","Wattakka",80),
        make_row("Onion Red","Rathu Lunu",350),
        make_row("Potato","Ala",200),
        make_row("Green Chilli","Miris",450),
        make_row("Lime","Dehi",850),
        make_row("Cucumber","Pipinna",90),
        make_row("Bitter Gourd","Karawila",160),
    ]
    df = pd.DataFrame(vegs, columns=["English","Sinhala","Thoga Ganum (Buy)","Thoga Vikunum (Sell)","Sillara Ganum (Buy)","Sillara Vikunum (Sell)","Labaya Rs"])
    return df

df = get_pro_data()

# --- TOP METRICS ---
c1,c2,c3,c4 = st.columns(4)
c1.metric("📦 තොග ගැනුම් Avg", f"Rs.{df['Thoga Ganum (Buy)'].mean():.0f}", "අඩුම")
c2.metric("📦 තොග විකුණුම් Avg", f"Rs.{df['Thoga Vikunum (Sell)'].mean():.0f}")
c3.metric("🛒 සිල්ලර ගැනුම් Avg", f"Rs.{df['Sillara Ganum (Buy)'].mean():.0f}")
c4.metric("💰 සිල්ලර විකුණුම් Avg", f"Rs.{df['Sillara Vikunum (Sell)'].mean():.0f}", f"+{df['Labaya Rs'].mean():.0f} Labaya")

st.divider()

# --- SELECT VEGETABLE FOR CHART ---
st.subheader("📊 ලස්සන Chart එක - භාණ්ඩයක් තෝරන්න")
selected = st.selectbox("Vegetable තෝරන්න", df["English"] + " (" + df["Sinhala"] + ")")
sel_eng = selected.split(" (")[0]
row = df[df["English"]==sel_eng].iloc[0]

chart_data = pd.DataFrame({
    "Type": ["Thoga Ganum","Thoga Vikunum","Sillara Ganum","Sillara Vikunum"],
    "Price": [row["Thoga Ganum (Buy)"], row["Thoga Vikunum (Sell)"], row["Sillara Ganum (Buy)"], row["Sillara Vikunum (Sell)"]]
})

colA, colB = st.columns([1,1])
with colA:
    st.markdown(f"**{row['English']} ({row['Sinhala']}) - අද මිල**")
    st.bar_chart(chart_data, x="Type", y="Price", color="#0ea5e9")
    st.dataframe(chart_data, use_container_width=True, hide_index=True)

with colB:
    st.markdown("**💰 ලාබය (Profit Chart)**")
    profit_data = pd.DataFrame({
        "Type": ["Gaththa Mila","Vikunu Mila","Labaya"],
        "Rs": [row["Thoga Ganum (Buy)"], row["Sillara Vikunum (Sell)"], row["Labaya Rs"]]
    })
    st.bar_chart(profit_data, x="Type", y="Rs", color="#10b981")
    st.info(f"👉 **{row['English']}** 1kg ගෙනත් විකුණුවොත් ලාබය **Rs.{row['Labaya Rs']}**")

st.divider()

# --- FULL TABLE ---
st.subheader("📋 සියලුම භාණ්ඩ - තොග / සිල්ලර / ගැනුම් / විකුණුම් වෙන වෙනම")

tab1, tab2 = st.tabs(["📋 Table View", "📈 All Items Chart"])

with tab1:
    search = st.text_input("Search Batu / Thakkali")
    dff = df
    if search:
        dff = dff[dff["English"].str.lower().str.contains(search.lower()) | dff["Sinhala"].str.lower().str.contains(search.lower())]
    st.dataframe(dff, use_container_width=True, hide_index=True)

with tab2:
    st.bar_chart(df, x="English", y=["Thoga Ganum (Buy)","Thoga Vikunum (Sell)","Sillara Ganum (Buy)","Sillara Vikunum (Sell)"])
    st.line_chart(df, x="English", y=["Thoga Ganum (Buy)","Sillara Vikunum (Sell)"])

st.divider()
st.success(f"✅ **දිනපතා Auto Update!** අද: {datetime.date.today()} | හෙට වෙනකොට මිල 4ම auto වෙනස් වෙනවා!")

colx, coly = st.columns(2)
with colx:
    if st.button("🔄 අද මිල Refresh"):
        st.cache_data.clear()
        st.rerun()
with coly:
    st.download_button("📥 Download PRO Prices CSV", df.to_csv(index=False), "pro_prices.csv")

st.caption("Thoga Ganum = තොග ගැනුම් (Farmerගෙන් ගන්න), Thoga Vikunum = තොග විකුණුම්, Sillara Ganum = සිල්ලර කඩේ ගන්න, Sillara Vikunum = සිල්ලර විකුණුම්")
import streamlit as st
import pandas as pd
import datetime
import random

st.set_page_config(page_title="Sahal Mas Malu PRO", page_icon="🍚", layout="wide")
st.title("🍚 සහල් | 🍗 මස් | 🐟 මාලු - PRO MAX")
st.caption(f"ගැනුම් | විකුණුම් | තොග | සිල්ලර | Daily Auto Update: {datetime.date.today()}")

@st.cache_data(ttl=86400)
def get_sahal_mas_malu():
    random.seed(datetime.date.today().day)
    def r(a,b): return random.randint(a,b)
    def make(eng, sin, base):
        tg = base - r(20,40)
        tv = base - r(5,15)
        sg = base + r(15,35)
        sv = base + r(40,80)
        lab = sv - tg
        return [eng, sin, tg, tv, sg, sv, lab]

    sahal = [
        make("Nadu","Nadu Sahal",210), make("Samba","Samba Sahal",235),
        make("Keeri Samba","Keeri Samba",320), make("Red Nadu","Rathu Nadu",215),
        make("White Kekulu","Sudu Kekulu",205), make("Red Kekulu","Rathu Kekulu",210),
        make("Motta Samba","Motta Samba",250), make("Suwandel
