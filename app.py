import streamlit as st
from astro_api import get_daily_horoscope
from utils import get_zodiac_sign
from cities import city_list  # import the cities

st.set_page_config(page_title="Daily Horoscope", layout="centered")

st.title("🔮 Astrology Daily Horoscope")
st.write("Enter your birth details to receive your daily horoscope and a short birth chart summary.")

# --- Birth Input Form ---
with st.form("birth_form"):
    name = st.text_input("Name")
    dob = st.date_input("Date of Birth")
    tob = st.time_input("Time of Birth")
    place = st.selectbox("Place of Birth", city_list)  # searchable dropdown
    submitted = st.form_submit_button("Get Horoscope")

# --- Show results if form is submitted ---
if submitted:
    zodiac_sign = get_zodiac_sign(dob)
    st.success(f"Zodiac Sign: {zodiac_sign}")

    st.subheader("🌟 Your Daily Horoscope")
    horoscope = get_daily_horoscope(zodiac_sign)
    st.write(horoscope)

    st.subheader("🗺️ Birth Chart Summary")
