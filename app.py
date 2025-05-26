import streamlit as st
import requests
from datetime import datetime
import os
from dotenv import load_dotenv

# Load your Prokerala credentials from .env file
load_dotenv()
API_KEY = os.getenv("4208ea20-bc34-4cc5-aa6b-9baa37463cb5")
API_SECRET = os.getenv("Xx8wAbZRRrKbfjXQvASwy0go9kBbsI7lkWXVttYr")

# Streamlit page config
st.set_page_config(page_title="Astrology Bot", layout="centered")
st.title("🔮 Astrology Daily Horoscope & Birth Chart")
st.write("Enter your birth details to get your horoscope and chart analysis.")

# --- Input Form ---
with st.form("astro_form"):
    name = st.text_input("Your Name")
    dob = st.date_input("Date of Birth")
    tob = st.time_input("Time of Birth")
    latitude = st.number_input("Latitude (e.g. 28.6139 for Delhi)", format="%.4f")
    longitude = st.number_input("Longitude (e.g. 77.2090 for Delhi)", format="%.4f")
    timezone = st.number_input("Time Zone (IST = 5.5)", value=5.5)
    submit = st.form_submit_button("Get My Horoscope")

# --- After Submit ---
if submit:
    datetime_str = f"{dob} {tob}"
    dt = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")

    st.success(f"Hello {name}! Here's your astrology report.")

    # --- Daily Horoscope ---
    st.subheader("🌟 Daily Horoscope")
    try:
        horoscope_url = "https://api.prokerala.com/v2/astrology/daily-horoscope"
        headers = {
            "Authorization": f"Basic {API_KEY}:{API_SECRET}"
        }
        horoscope_params = {
            "sign": "",  # Optional: You can detect sign based on date
            "datetime": dt.isoformat(),
            "timezone": timezone
        }
        # If you know the zodiac sign, add it here as `sign: "aries"` etc.
        horoscope_response = requests.get(horoscope_url, headers=headers, params=horoscope_params)
        horoscope_data = horoscope_response.json()

        if "horoscope" in horoscope_data:
            st.markdown(horoscope_data["horoscope"]["prediction"])
        else:
            st.warning("Could not fetch horoscope from Prokerala.")
    except Exception as e:
        st.error(f"Horoscope error: {e}")

    # --- Birth Chart ---
    st.subheader("🗺️ Birth Chart Summary")
    try:
        chart_url = "https://api.prokerala.com/v2/astrology/birth-chart"
        chart_params = {
            "datetime": dt.isoformat(),
            "latitude": latitude,
            "longitude": longitude,
            "timezone": timezone,
        }
        chart_response = requests.get(chart_url, headers=headers, params=chart_params)
        chart_data = chart_response.json()

        if "chart" in chart_data:
            for planet in chart_data["chart"]["planetaryPositions"]:
                st.markdown(f"**{planet['planet']['name']}** — in {planet['rasi']['name']} ({planet['house']['name']} House)")
        else:
            st.warning("Could not generate birth chart.")
    except Exception as e:
        st.error(f"Birth chart error: {e}")
