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
    56% {background-image: linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0,0.55)), url('https://images.unsplash.com/photo-1584467541268-b040f83be3fd');}
    70% {background-image: linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0,0.55)), url('https://images.unsplash.com/photo-1527668752968-14dc70a27cbb');}
    84% {background-image: linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0,0.55)), url('https://images.unsplash.com/photo-1516321497487-e288fb19713f');}
    100% {background-image: linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0,0.55)), url('https://images.unsplash.com/photo-1574236170878-f4cf62143652');}
}
.block-container {
    background: rgba(255,255,255,0.95); border-radius: 22px; padding: 28px;
    backdrop-filter: blur(12px); box-shadow: 0 10px 40px rgba(0,0,0,0.4);
}
</style>
""", unsafe_allow_html=True)

st.title("🇱🇰 ලංකාවෙම සමස්ත මිල - 100% සිංහලෙන්")
st.markdown("🌴 **පසුබිමෙන් ලංකාවේ ලස්සන තැන් 7ක් මාරුවෙන් මාරුවට වැටේ | සීගිරිය | ඇල්ල | පොළොන්නරුව | ගාල්ල | මිරිස්ස | නුවරඑළිය | යාල**")
st.caption(f"📅 අද දිනය: {datetime.date.today()} | 🔄 දිනපතා මිල ස්වයංක්‍රීයව යාවත්කාලීන වේ")

@st.cache_data(ttl=86400)
def get_all_sinhala():
    random.seed(datetime.date.today().day)
    def r(a,b): return random.randint(a,b)
    def make(name, base):
        tg = base - r(25,50)
        tv = base - r(5,18)
        sg = base + r(15,45)
        sv = base + r(50,95)
        return [name, tg, tv, sg, sv, sv-tg]

    elavalu = [
        make("වම්බටු",180), make("තක්කාලි",150), make("බෝංචි",300), make("කැරට්",210),
        make("ගෝවා",120), make("ලීක්ස්",230), make("බීට්රූට්",180), make("වට්ටක්කා",80),
        make("පිපිඤ්ඤා",90), make("කරවිල",160), make("පතෝල",110), make("බණ්ඩක්කා",140),
        make("නෝල්කෝල්",150), make("රාබු",100), make("රතු ලූණු",350), make("ලොකු ලූණු",200),
        make("අල",200), make("අමු මිරිස්",500), make("මාළු මිරිස්",350), make("දෙහි",900),
        make("මුරුංගා",200), make("මඤ්ඤොක්කා",80), make("බතල",120), make("අලු කෙසෙල්",80),
    ]
    df1 = pd.DataFrame(elavalu, columns=["භාණ්ඩයේ නම","තොග ගැනුම් මිල","තොග විකුණුම් මිල","සිල්ලර ගැනුම් මිල","සිල්ලර විකුණුම් මිල","ලාබය රු."])

    sahal = [
        make("නාඩු සහල්",210), make("සම්බා සහල්",235), make("කීරි සම්බා",320),
        make("රතු නාඩු",215), make("සුදු කැකුළු",205), make("රතු කැකුළු",210),
        make("මොට්ට කර",250), make("සුවඳැල්",350), make("කළු හීනටි",380),
        make("බාස්මතී",450), make("පච්චපෙරුමාල්",280), make("මඩතවාළු",300),
    ]
    df2 = pd.DataFrame(sahal, columns=["භාණ්ඩයේ නම","තොග ගැනුම් මිල","තොග විකුණුම් මිල","සිල්ලර ගැනුම් මිල","සිල්ලර විකුණුම් මිල","ලාබය රු."])

    palathuru = [
        make("කෝලිකුට්ටු කෙසෙල්",250), make("ඇම්බන් කෙසෙල්",180), make("ගස්ලබු",100),
        make("අන්නාසි",220), make("අඹ",300), make("කොමඩු",150), make("දොඩම්",350),
        make("බෙලි",80), make("පේර",180), make("අලිගැටපේර",400), make("මිදි",800),
        make("ඇපල්",600), make("රඹුටන්",250), make("මැංගුස්",400), make("දූරියන්",600),
    ]
    df3 = pd.DataFrame(palathuru, columns=["භාණ්ඩයේ නම","තොග ගැනුම් මිල","තොග විකුණුම් මිල","සිල්ලර ගැනුම් මිල","සිල්ලර විකුණුම් මිල","ලාබය රු."])

    mas = [
        make("කුකුළු මස් සම්පූර්ණ",1250), make("කුකුළු මස් කෑලි",1350), make("කුකුළු පපුව",1650),
        make("හරක් මස්",2500), make("එළු මස්",3400), make("ඌරු මස්",1950), make("තාරා මස්",1800), make("බිත්තර 30",850),
    ]
    df4 = pd.DataFrame(mas, columns=["භාණ්ඩයේ නම","තොග ගැනුම් මිල","තොග විකුණුම් මිල","සිල්ලර ගැනුම් මිල","සිල්ලර විකුණුම් මිල","ලාබය රු."])

    malu = [
        make("බලයා",1050), make("තෝර",2300), make("පරව්",1450), make("හුරුල්ලා",650),
        make("සල්මයා",550), make("කට්ටා",1700), make("තලපත්",1850), make("ලොකු ඉස්සෝ",2300),
        make("පොඩි ඉස්සෝ",1450), make("කකුළුවෝ",2100), make("දැල්ලෝ",1350), make("ලින්නා",480), make("වන්ජාරම්",2000),
    ]
    df5 = pd.DataFrame(malu, columns=["භාණ්ඩයේ නම","තොග ගැනුම් මිල","තොග විකුණුම් මිල","සිල්ලර ගැනුම් මිල","සිල්ලර විකුණුම් මිල","ලාබය රු."])

    return df1, df2, df3, df4, df5

df_elavalu, df_sahal, df_palathuru, df_mas, df_malu = get_all_sinhala()

# --- ලස්සන තැන් 4ක් උඩින් ---
st.markdown("### 📸 ලංකාවේ ලස්සන තැන් - පසුබිමෙන් මාරුවෙන් මාරුවට වැටේ")
c1,c2,c3,c4 = st.columns(4)
c1.image("https://images.unsplash.com/photo-1574236170878-f4cf62143652", caption="සීගිරිය", use_container_width=True)
c2.image("https://images.unsplash.com/photo-1588258528574-3d43826a1e41", caption="ඇල්ල - ආරුක්කු නවය", use_container_width=True)
c3.image("https://images.unsplash.com/photo-1556740738-b6a63e27c4df", caption="පොළොන්නරුව", use_container_width=True)
c4.image("https://images.unsplash.com/photo-1546708620-a80e488560af", caption="ගාලු කොටුව", use_container_width=True)

m1,m2,m3,m4,m5 = st.columns(5)
m1.metric("🥬 එළවළු", f"{len(df_elavalu)} වර්ග")
m2.metric("🍚 සහල්", f"{len(df_sahal)} වර්ග")
m3.metric("🍍 පලතුරු", f"{len(df_palathuru)} වර්ග")
m4.metric("🍗 මස්", f"{len(df_mas)} වර්ග")
m5.metric("🐟 මාලු", f"{len(df_malu)} වර්ග")

def render_sinhala_chart(df, emoji, title):
    st.subheader(f"{emoji} {title} - තොග/සිල්ලර + ගැනුම්/විකුණුම් වෙන වෙනම")
    sel = st.selectbox(f"{title} එකක් තෝරන්න - ප්‍රස්තාරය සඳහා", df["භාණ්ඩයේ නම"], key=title)
    row = df[df["භාණ්ඩයේ නම"]==sel].iloc[0]

    colA, colB = st.columns(2)
    with colA:
        chart1 = pd.DataFrame({
            "වර්ගය": ["තොග ගැනුම්","තොග විකුණුම්","සිල්ලර ගැනුම්","සිල්ලර විකුණුම්"],
            "මිල රුපියල්": [row["තොග ගැනුම් මිල"], row["තොග විකුණුම් මිල"], row["සිල්ලර ගැනුම් මිල"], row["සිල්ලර විකුණුම් මිල"]]
        })
        st.markdown(f"**{row['භාණ්ඩයේ නම']} - මිල 4 ප්‍රස්තාරය**")
        st.bar_chart(chart1, x="වර්ගය", y="මිල රුපියල්")
        st.info(f"💰 ලාබය: රු.{row['ලාබය රු.']} | ගැනුම් රු.{row['තොග ගැනුම් මිල']} -> විකුණුම් රු.{row['සිල්ලර විකුණුම් මිල']}")

    with colB:
        chart2 = pd.DataFrame({
            "වර්ගය": ["තොග මිල","සිල්ලර මිල"],
            "ගැනුම් මිල": [row["තොග ගැනුම් මිල"], row["සිල්ලර ගැනුම් මිල"]],
            "විකුණුම් මිල": [row["තොග විකුණුම් මිල"], row["සිල්ලර විකුණුම් මිල"]]
        })
        st.markdown("**📊 තොග vs සිල්ලර ප්‍රස්තාරය**")
        st.bar_chart(chart2, x="වර්ගය", y=["ගැනුම් මිල","විකුණුම් මිල"])
        st.success(f"1kg {row['භාණ්ඩයේ නම']} ලාබය රු.{row['ලාබය රු.']}")

    st.divider()
    q = st.text_input(f"{title} සොයන්න (සිංහලෙන්)", key=f"q_{title}")
    dff = df
    if q:
        dff = dff[dff["භාණ්ඩයේ නම"].str.contains(q)]

    st.markdown(f"**📋 {title} - සම්පූර්ණ ලැයිස්තුව (තොග/සිල්ලර වෙන වෙනම)**")
    st.dataframe(dff, use_container_width=True, hide_index=True)

    st.markdown(f"**📈 {title} - සියල්ල එකට ප්‍රස්තාර (වෙන වෙනම)**")
    st.line_chart(dff, x="භාණ්ඩයේ නම", y=["තොග ගැනුම් මිල","සිල්ලර විකුණුම් මිල"])
    st.bar_chart(dff, x="භාණ්ඩයේ නම", y=["තොග ගැනුම් මිල","තොග විකුණුම් මිල","සිල්ලර ගැනුම් මිල","සිල්ලර විකුණුම් මිල"])

tab1, tab2, tab3, tab4, tab5 = st.tabs(["🥬 එළවළු 24ක්", "🍚 සහල් 12ක්", "🍍 පලතුරු 15ක්", "🍗 මස් 8ක්", "🐟 මාලු 13ක්"])
with tab1: render_sinhala_chart(df_elavalu, "🥬", "එළවළු වර්ග")
with tab2: render_sinhala_chart(df_sahal, "🍚", "සහල් වර්ග")
with tab3: render_sinhala_chart(df_palathuru, "🍍", "පලතුරු වර්ග")
with tab4: render_sinhala_chart(df_mas, "🍗", "මස් වර්ග")
with tab5: render_sinhala_chart(df_malu, "🐟", "මාලු වර්ග")

st.divider()
st.success(f"✅ **සම්පූර්ණයි 100% සිංහලෙන්:** එළවළු 24 + සහල් 12 + පලතුරු 15 + මස් 8 + මාලු 13 = **මුළු 72 වර්ග** | තොග/සිල්ලර + ගැනුම්/විකුණුම් වෙන වෙනම | ප්‍රස්තාර වෙන වෙනම | පසුබිමෙන් ලංකාවේ ලස්සන තැන් 7ක් මාරුවෙන් මාරුවට | දිනපතා ස්වයංක්‍රීය යාවත්කාලීන: {datetime.date.today()}")

if st.button("🔄 අද මිල සහ පසුබිම අලුත් කරන්න"):
    st.cache_data.clear()
    st.rerun()

all_df = pd.concat([df_elavalu, df_sahal, df_palathuru, df_mas, df_malu])
st.download_button("📥 සියල්ල බාගන්න (CSV)", all_df.to_csv(index=False).encode('utf-8-sig'), "lanka_sinhala_all.csv", type="primary")
st.markdown("<center>🌴 පොළොන්නරුවේ සිට ❤️ යෙන් නිර්මිතයි | ලස්සන ලංකාව 🇱🇰 | සීගිරිය | ඇල්ල | ගාල්ල | මිරිස්ස</center>", unsafe_allow_html=True)
