import streamlit as st
from astro_api import get_daily_horoscope, get_birth_chart
from utils import get_answer, get_zodiac_sign

st.set_page_config(page_title="Astrology Birth Chart GPT", page_icon="🔮", layout="centered")

st.markdown("<h1 style='text-align: center;'>Astrology Birth Chart GPT</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Expert astrologer GPT that needs your birth info to answer queries.</p>", unsafe_allow_html=True)

st.markdown("---")

if 'form_submitted' not in st.session_state:
    st.session_state['form_submitted'] = False

with st.form("birth_form"):
    st.markdown("### 🗓️ Enter Your Birth Details")
    name = st.text_input("Name")
    date_of_birth = st.date_input("Date of Birth")
    time_of_birth = st.time_input("Time of Birth")
    birth_place = st.text_input("Place of Birth")
    submitted = st.form_submit_button("Submit")
    if submitted:
        zodiac_sign = get_zodiac_sign(date_of_birth)
        st.session_state['form_submitted'] = True
        st.session_state['birth_details'] = {
            "name": name,
            "dob": date_of_birth,
            "tob": time_of_birth,
            "place": birth_place,
            "sign": zodiac_sign
        }

if st.session_state.get('form_submitted'):
    
