import streamlit as st
from astro_api import get_daily_horoscope, get_birth_chart
from utils import get_zodiac_sign

st.set_page_config(page_title="Daily Horoscope", layout="centered")

st.title("🔮 Astrology Daily Horoscope")
st.write("Get your free daily horoscope and a brief birth chart reading.")

with st.form("birth_form"):
    name = st.text_input("Name")
    dob = st.date_input("Date of Birth")
    tob = st.time_input("Time of Birth")
    place = st.text_input("Place of Birth")
    submitted = st.form_submit_button("Get Horoscope")

if submitted:
    zodiac_sign = get_zodiac_sign(dob)
    st.success(f"Zodiac Sign: {zodiac_sign}")

    st.subheader("🌟 Your Daily Horoscope")
    horoscope = get_daily_horoscope(zodiac_sign)
    st.write(horoscope)

    st.subheader("🗺️ Short Birth Chart Summary")
    birth_chart = get_birth_chart(name, dob, tob, place)
    st.write(birth_chart)
