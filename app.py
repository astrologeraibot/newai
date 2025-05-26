import streamlit as st
from datetime import date, time, datetime
import random

st.set_page_config(page_title="Astrology Bot", layout="centered")
st.title("🔮 Offline Astrology Bot")
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

# ---------------------- Horoscope Content ----------------------
horoscope_data = {
    "aries": {
        "general": "🔥 Take the lead! Your natural courage will open new doors today.",
        "love": "💘 Romance is blooming — express your heart boldly.",
        "career": "🚀 A great day to pitch ideas or ask for a promotion.",
        "health": "💪 Energy is high. Use it for something physical.",
        "color": "Red ❤️",
        "number": "9"
    },
    "taurus": {
        "general": "🌿 Slow and steady wins the race. Be patient with results.",
        "love": "💞 Loyalty matters. Express appreciation to your partner.",
        "career": "📈 Stick to routines — steady growth is coming.",
        "health": "🧘 Relaxation will boost your mental health.",
        "color": "Green 🍀",
        "number": "6"
    },
    "gemini": {
        "general": "🧠 Mental clarity helps you solve long-standing issues.",
        "love": "💌 Flirty chats may lead to something deeper.",
        "career": "🗣️ Communicate clearly to avoid misunderstandings.",
        "health": "😴 You may feel drained. Prioritize rest.",
        "color": "Yellow 🌟",
        "number": "5"
    },
    "cancer": {
        "general": "🌊 Emotions run deep — honor them without judgment.",
        "love": "👩‍❤️‍👨 Heartfelt connection is possible today.",
        "career": "🏠 Home-based work brings unexpected success.",
        "health": "🥗 Take care of digestion. Avoid overeating.",
        "color": "Silver 🌙",
        "number": "2"
    },
    "leo": {
        "general": "🦁 Shine your light — others will follow.",
        "love": "💖 Attraction is strong. Take the first move.",
        "career": "🎤 You’re in the spotlight. Show your skills.",
        "health": "🏋️‍♂️ Great day for physical fitness or sports.",
        "color": "Gold ✨",
        "number": "1"
    },
    "virgo": {
        "general": "📋 Organization is key today. Make to-do lists.",
        "love": "💗 Pay attention to small romantic gestures.",
        "career": "📊 Details matter — perfect time for audits or edits.",
        "health": "🧼 Clean eating will improve your mood.",
        "color": "Beige 🤎",
        "number": "4"
    },
    "libra": {
        "general": "⚖️ Balance is your superpower — restore harmony.",
        "love": "💝 Relationships deepen through empathy today.",
        "career": "💼 Collaborations bring creative results.",
        "health": "🧘 Practice yoga or meditation.",
        "color": "Pink 🌸",
        "number": "7"
    },
    "scorpio": {
        "general": "🦂 Intuition is sharp. Trust your gut feeling.",
        "love": "💋 Passionate moments await.",
        "career": "🔍 Look beneath the surface — secrets may emerge.",
        "health": "🩺 Watch for emotional stress.",
        "color": "Black 🖤",
        "number": "8"
    },
    "sagittarius": {
        "general": "🏹 Expand your horizons — learn something new.",
        "love": "💬 Honest conversations lead to love.",
        "career": "🌍 Opportunities abroad or online look promising.",
        "health": "🚴 Move your body and explore.",
        "color": "Purple 🔮",
        "number": "3"
    },
    "capricorn": {
        "general": "📈 Hard work pays off. Keep climbing.",
        "love": "🤎 Stability is sexy. Build something lasting.",
        "career": "🧱 Step-by-step progress toward goals.",
        "health": "💤 Don’t neglect sleep.",
        "color": "Brown 🪵",
        "number": "10"
    },
    "aquarius": {
        "general": "🔮 Think different. Innovation is your edge.",
        "love": "🌐 Love may spark in unusual places.",
        "career": "👽 Tech and creative fields thrive today.",
        "health": "🧠 Stimulate your mind, avoid boredom.",
        "color": "Blue 🌊",
        "number": "11"
    },
    "pisces": {
        "general": "🎨 Let your imagination guide your day.",
        "love": "💫 Romantic dreams feel real today.",
        "career": "🎭 Creative projects shine.",
        "health": "🛀 Take a long bath or meditate.",
        "color": "Sea green 🧜",
        "number": "12"
    },
}

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
    data = horoscope_data[zodiac]

    st.success(f"🌞 **Hello {name}, your Zodiac Sign is `{zodiac.title()}`**")

    st.subheader("🌟 Daily Horoscope")
    st.markdown(f"""
    **{data['general']}**

    ❤️ **Love**: {data['love']}  
    💼 **Career**: {data['career']}  
    🩺 **Health**: {data['health']}  
    🎨 **Lucky Color**: `{data['color']}`  
    🔢 **Lucky Number**: `{data['number']}`  
    """)

    st.subheader("🗺️ Basic Birth Chart Summary")
    st.markdown(f"""
    - 🗓️ **Date of Birth**: `{dob.strftime('%B %d, %Y')}`
    - ⏰ **Time of Birth**: `{tob.strftime('%I:%M %p')}`
    - 🌟 **Zodiac Sign**: `{zodiac.title()}`
    - 💫 **Key Traits**: {zodiac_traits[zodiac]}
    """)

