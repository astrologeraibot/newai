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
       # --- Daily Horoscope ---
    st.subheader("🌟 Daily Horoscope")
    try:
        # Get zodiac sign based on DOB
        def get_zodiac_sign(day, month):
            zodiac_signs = [
                (120, 'Capricorn'), (218, 'Aquarius'), (320, 'Pisces'),
                (420, 'Aries'), (521, 'Taurus'), (621, 'Gemini'),
                (722, 'Cancer'), (823, 'Leo'), (923, 'Virgo'),
                (1023, 'Libra'), (1122, 'Scorpio'), (1222, 'Sagittarius'), (1231, 'Capricorn')
            ]
            date_number = month * 100 + day
            for cutoff, sign in zodiac_signs:
                if date_number <= cutoff:
                    return sign.lower()
            return "capricorn"

        zodiac_sign = get_zodiac_sign(dob.day, dob.month)

        horoscope_url = f"https://api.prokerala.com/v2/astrology/daily-horoscope/{zodiac_sign.lower()}"
        headers = {
            "Authorization": f"Basic {API_KEY}:{API_SECRET}"
        }

        response = requests.get(horoscope_url, headers=headers)
        data = response.json()

        if "horoscope" in data:
            st.markdown(data["horoscope"]["prediction"])
        else:
            st.warning("Could not get horoscope. Check API key or limit.")

    except Exception as e:
        st.error(f"Error getting horoscope: {e}")

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
