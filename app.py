import streamlit as st
from datetime import date, time
import random
import io

st.set_page_config(page_title="Astrologer Bot", layout="centered")
st.title("🔮 Astrologer Bot")
st.markdown("Enter your birth details to receive your **daily horoscope**, **lucky traits**, and a basic **birth chart summary** — no APIs needed!")

# ---------------------- Zodiac Logic ----------------------
def get_zodiac_sign(dob):
    day, month = dob.day, dob.month
    if (month == 12 and day >= 22) or (month == 1 and day <= 19): return "capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18): return "aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20): return "pisces"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19): return "aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20): return "taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20): return "gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22): return "cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22): return "leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22): return "virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22): return "libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21): return "scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21): return "sagittarius"

# Emoji per zodiac sign
zodiac_emojis = {
    "aries": "♈",
    "taurus": "♉",
    "gemini": "♊",
    "cancer": "♋",
    "leo": "♌",
    "virgo": "♍",
    "libra": "♎",
    "scorpio": "♏",
    "sagittarius": "♐",
    "capricorn": "♑",
    "aquarius": "♒",
    "pisces": "♓"
}

# ---------------------- Horoscope Data & Traits ----------------------
# (Insert your `daily_horoscopes` and `zodiac_traits` dictionaries here—unchanged)

# Sample traits dictionary (shortened for demo)
zodiac_traits = {
    "aries": "Bold 🔥 | Confident 💪 | Adventurous 🌍",
    "taurus": "Patient 🌿 | Loyal 🐂 | Stable 🪨",
    "gemini": "Witty 🧠 | Curious 🤔 | Versatile 💫",
    "cancer": "Emotional 💧 | Intuitive 🌙 | Nurturing 🐚",
    "leo": "Confident 👑 | Generous 💛 | Leader 🦁",
    "virgo": "Practical 📋 | Helpful 🧹 | Analytical 🧐",
    "libra": "Charming 🌸 | Peaceful ⚖️ | Romantic 💘",
    "scorpio": "Passionate 🦂 | Intense 🔥 | Mysterious 🕵️",
    "sagittarius": "Adventurous 🏹 | Optimistic 🌈 | Honest 💬",
    "capricorn": "Ambitious 📈 | Wise 🐐 | Disciplined ⏳",
    "aquarius": "Innovative 🧪 | Free-spirited 🌬️ | Visionary 🌐",
    "pisces": "Dreamy 🐠 | Compassionate 💗 | Artistic 🎨"
}

# ---------------------- UI Form ----------------------
with st.form("astro_form"):
    name = st.text_input("Your Name")
    dob = st.date_input("Date of Birth")
    tob = st.time_input("Time of Birth", value=time(12, 0))
    submitted = st.form_submit_button("🔍 Reveal Horoscope")

if submitted:
    zodiac = get_zodiac_sign(dob)
    emoji = zodiac_emojis[zodiac]
    data = daily_horoscopes[zodiac]
    traits = zodiac_traits[zodiac]

    st.success(f"{emoji} Hello {name}, your Zodiac Sign is **{zodiac.title()}**!")

    st.subheader("🌟 Daily Horoscope")
    st.markdown(f"""
**{data['general']}**

❤️ **Love**: {data['love']}  
💼 **Career**: {data['career']}  
🩺 **Health**: {data['health']}  
🎨 **Lucky Color**: {data['color']}  
🔢 **Lucky Number**: {data['number']}  
""")

    st.subheader("🧬 Zodiac Personality Traits")
    st.info(f"**{traits}**")

    st.subheader("🗺️ Basic Birth Chart Summary")
    birth_summary = f"""
🗓️ Date of Birth: {dob.strftime('%B %d, %Y')}
⏰ Time of Birth: {tob.strftime('%I:%M %p')}
🌞 Sun Sign: {zodiac.title()} {emoji}
📍 (Moon, Ascendant, and Planets not shown in this basic version)
"""
    st.code(birth_summary)

    # Create text content for download
    text_output = f"""
🔮 Horoscope Report for {name}
==============================

Zodiac Sign: {zodiac.title()} {emoji}

🌟 Daily Horoscope
-------------------
{data['general']}

❤️ Love: {data['love']}
💼 Career: {data['career']}
🩺 Health: {data['health']}
🎨 Lucky Color: {data['color']}
🔢 Lucky Number: {data['number']}

🧬 Zodiac Personality Traits
-----------------------------
{traits}

🗺️ Basic Birth Chart Summary
-----------------------------
Date of Birth: {dob.strftime('%B %d, %Y')}
Time of Birth: {tob.strftime('%I:%M %p')}
Sun Sign: {zodiac.title()} {emoji}
"""

    # Convert to bytes
    text_bytes = io.BytesIO(text_output.encode('utf-8'))

    st.download_button(
        label="📄 Download Horoscope as TXT",
        data=text_bytes,
        file_name=f"{name}_horoscope.txt",
        mime="text/plain"
    )
