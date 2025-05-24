import streamlit as st
from astro_api import get_daily_horoscope, get_birth_chart
from utils import get_answer

st.set_page_config(page_title="Astrology Birth Chart GPT", page_icon="🔮", layout="centered")

st.markdown("<h1 style='text-align: center;'>Astrology Birth Chart GPT</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Expert astrologer GPT that needs your birth info to answer queries.</p>", unsafe_allow_html=True)

st.markdown("---")

# Use session_state to persist submission
if 'form_submitted' not in st.session_state:
    st.session_state['form_submitted'] = False

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
        st.session_state['form_submitted'] = True
        st.session_state['birth_details'] = {
            "name": name,
            "dob": date_of_birth,
            "tob": time_of_birth,
            "place": birth_place,
            "sign": zodiac_sign
        }

# Show question input if form is submitted
if st.session_state.get('form_submitted'):
    st.success("Birth details submitted. Ask your question below!")
    
    user_input = st.text_input("Ask anything")

    if st.button("Get Answer"):
        user_input = user_input.strip()
        if user_input:
            with st.spinner("🔭 Analyzing your stars..."):
                details = st.session_state['birth_details']
                try:
                    if "horoscope" in user_input.lower():
                        result = get_daily_horoscope(details['sign'])
                    elif "birth chart" in user_input.lower():
                        result = get_birth_chart(
                            details['name'], details['dob'], details['tob'], details['place']
                        )
                    else:
                        result = get_answer(user_input, details['sign'])
                except Exception as e:
                    result = f"An error occurred: {str(e)}"
            st.markdown("### 📝 Answer:")
            st.write(result or "No response received.")
        else:
            st.warning("Please enter a question.")
