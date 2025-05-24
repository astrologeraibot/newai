import streamlit as st
from astro_api import get_daily_horoscope, get_birth_chart
from utils import predefined_questions, get_answer

st.set_page_config(page_title="Astrology Birth Chart GPT", page_icon="🔮", layout="centered")

st.markdown("<h1 style='text-align: center;'>Astrology Birth Chart GPT</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Expert astrologer GPT that needs your birth info to answer queries.</p>", unsafe_allow_html=True)

st.markdown("### 🔮 Quick Questions")
for question in predefined_questions:
    if st.button(question):
        st.session_state['user_input'] = question

st.markdown("---")

with st.form("birth_form"):
    st.markdown("### 🗓️ Enter Your Birth Details")
    name = st.text_input("Name")
    date_of_birth = st.date_input("Date of Birth")
    time_of_birth = st.time_input("Time of Birth")
    birth_place = st.text_input("Place of Birth")
    zodiac_sign = st.selectbox("Your Zodiac Sign", [
        "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
        "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
    ])
    submitted = st.form_submit_button("Submit")

if submitted:
    st.success("Birth details submitted. Ask your question below!")

    if 'user_input' not in st.session_state:
        st.session_state['user_input'] = ""

    user_input = st.text_input("Ask anything", value=st.session_state['user_input'])
    if st.button("Get Answer"):
    user_input = user_input.strip()
    if user_input:
        with st.spinner("🔭 Analyzing your stars..."):
            try:
                if "horoscope" in user_input.lower():
                    result = get_daily_horoscope(zodiac_sign)
                elif "birth chart" in user_input.lower():
                    result = get_birth_chart(name, date_of_birth, time_of_birth, birth_place)
                else:
                    result = get_answer(user_input, zodiac_sign)
            except Exception as e:
                result = f"An error occurred: {str(e)}"
        st.markdown("### 📝 Answer:")
        st.write(result or "No response received.")
    else:
        st.warning("Please enter a question.")
