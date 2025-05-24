import streamlit as st
from astro_api import get_daily_horoscope, get_birth_chart
from utils import get_answer

st.set_page_config(page_title="Astrology Chatbot", page_icon="🔮", layout="centered")

st.title("🔮 Astrology Birth Chart GPT")
st.write("Enter your birth details and ask anything about your horoscope, future, love life, and more.")

# Session to persist form submission
if 'form_submitted' not in st.session_state:
    st.session_state['form_submitted'] = False

with st.form("birth_form"):
    name = st.text_input("Name")
    dob = st.date_input("Date of Birth")
    tob = st.time_input("Time of Birth")
    place = st.text_input("Place of Birth")
    submitted = st.form_submit_button("Submit")
    if submitted:
        zodiac_sign = get_zodiac_sign(dob)
        st.session_state['form_submitted'] = True
        st.session_state['birth_details'] = {
            "name": name,
            "dob": dob,
            "tob": tob,
            "place": place,
            "sign": zodiac_sign
        }

# After birth details are submitted
if st.session_state.get('form_submitted'):
    details = st.session_state['birth_details']
    st.success(f"Birth details submitted. Detected sign: **{details['sign']}**")

    user_input = st.text_input("Ask anything")

    if st.button("Get Answer"):
        user_input = user_input.strip()
        if user_input:
            with st.spinner("🔭 Reading your stars..."):
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
            st.write(result or "No response.")
        else:
            st.warning("Please enter a question.")
