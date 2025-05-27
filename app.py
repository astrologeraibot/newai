import streamlit as st
from datetime import date, time, datetime
import random

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

# ---------------------- Horoscope Content ----------------------
daily_horoscopes = {
    "aries": {
        "general": "Today is a day of action, Aries. Your natural leadership is highlighted, and people around you will seek your guidance. Challenges may arise, but they are merely stepping stones to greater success. Stay alert and proactive—opportunities for growth, especially in creative or personal ventures, are closer than they appear.",
        "love": "Your passion runs high today, and emotional connections may deepen. Whether you're single or in a relationship, communication is key. Speak openly and from the heart. A meaningful gesture could spark joy and lead to stronger bonds.",
        "career": "Colleagues may rely on your initiative and energy. Step forward with confidence and don't hesitate to share your ideas. Leadership opportunities are within reach if you stay disciplined and collaborative.",
        "health": "Your physical energy is high, but don’t overdo it. Balanced meals and regular hydration will keep your stamina steady. Mental rest is just as important as physical exertion today.",
        "money": "You may feel tempted to spend on luxuries or gifts. While it’s okay to indulge a little, be mindful of your savings goals. A financial discussion with a mentor could lead to smarter budgeting.",
        "color": "Red 🔴",
        "number": "9"
    },
    "taurus": {
        "general": "Stability is your strength today, Taurus. Ground yourself in routine and responsibilities, and you’ll feel a strong sense of accomplishment. While others may rush around, your steady pace will win the race. This is a good day to focus on home matters or long-term planning.",
        "love": "Romance blossoms through simple, thoughtful acts. A quiet evening or heartfelt message will speak volumes. Singles may encounter someone who values sincerity over flair—keep your heart open.",
        "career": "Your reliability is noticed by higher-ups today. Use this to solidify your role and show that you can handle bigger responsibilities. Avoid office gossip—it distracts from your growing momentum.",
        "health": "You may feel slightly sluggish early in the day. Light stretching or yoga will reenergize you. Watch out for sugar cravings; stick to balanced meals for consistent energy.",
        "money": "Today favors reviewing investments and spending habits. Avoid impulsive purchases and focus on necessities. A small financial tip from a trusted source could be valuable long-term.",
        "color": "Green 🟢",
        "number": "6"
    },
    "gemini": {
        "general": "Today your curiosity is off the charts, Gemini. New ideas spark easily and you're full of quick wit and clever responses. It’s a good day for learning, writing, or brainstorming creative projects. But avoid scattering your energy across too many things. Focus will bring true progress.",
        "love": "Communication in relationships is strong. Express yourself clearly and listen deeply to others. Singles may find a spark through intellectual connections—don’t ignore someone who stimulates your mind.",
        "career": "This is the time to speak up in meetings or pitch innovative ideas. Your communication skills impress others today. Stay organized so you don’t lose track of key details.",
        "health": "Mental stimulation is great, but your body needs care too. Take breaks from screens and stretch often. Light cardio or a short walk will balance your mental energy.",
        "money": "Be cautious with spontaneous purchases. You may be tempted by gadgets or subscriptions. Hold off and evaluate their real value before spending.",
        "color": "Yellow 💛",
        "number": "5"
    },
    "cancer": {
        "general": "Emotions run deep today, Cancer. You may feel more introspective, which is a great opportunity to journal or meditate. Trust your intuition—it will guide you well in decision-making. Focus on creating a safe, nurturing environment for yourself and loved ones.",
        "love": "Affection is strong today, but avoid overreacting to small issues. If something feels off, speak gently and with care. Couples can benefit from cozy time together. Singles may find comfort in reconnecting with someone from the past.",
        "career": "Let your empathy shine at work—it may help resolve a long-standing issue. Teamwork will flow better if you trust others and delegate properly.",
        "health": "Take care of your emotional wellness. Drink soothing teas, avoid emotional eating, and practice grounding exercises if you're feeling overwhelmed.",
        "money": "Today’s not the best day for risk-taking financially. Stick to your budget and avoid lending money unless it’s necessary. Stability comes through careful planning.",
        "color": "Silver ⚪",
        "number": "2"
    },
    "leo": {
        "general": "Your charisma is on fire today, Leo. You naturally attract attention and admiration, so use it wisely. This is a good time to express your talents, whether in work, hobbies, or social settings. Just beware of ego clashes and remember to lift others up too.",
        "love": "You’re feeling romantic and confident, which can heat things up. Plan something dramatic or fun with your partner. If single, your magnetic presence may draw someone bold your way.",
        "career": "Be the leader your team needs today. Your confidence can rally people around a common goal. Be open to feedback—great leaders listen too.",
        "health": "Avoid burnout by balancing activity with relaxation. Your energy is high, but your heart needs time to rest and reset.",
        "money": "You may be inspired to spend on something flashy. Check your finances first—this could either be a rewarding treat or an unnecessary drain.",
        "color": "Gold 🟡",
        "number": "1"
    },
    "virgo": {
        "general": "You’re detail-oriented today, Virgo, and it pays off. Your ability to analyze and sort out issues will help you navigate both personal and professional matters. Don’t let perfectionism slow you down—focus on progress, not flawlessness.",
        "love": "Small gestures mean a lot. Leave a sweet note, prepare a meal, or listen attentively. If single, an unexpected conversation may hint at romantic potential—don’t ignore subtle signals.",
        "career": "Today is excellent for reviewing reports, fine-tuning projects, and organizing your workspace. Your boss may recognize your diligence.",
        "health": "Digestive issues might flare up—choose light, clean meals. A walk in nature could ease stress and sharpen your mind.",
        "money": "A review of your financial documents may reveal a minor oversight or an opportunity to save. Avoid impulse purchases and stick to your plan.",
        "color": "Brown 🟤",
        "number": "4"
    },
    "libra": {
        "general": "Balance is everything for you today, Libra. You may be called to mediate a disagreement or restore harmony where there is chaos. Your charm and diplomacy will work wonders. Spend some time beautifying your space—it will soothe your soul.",
        "love": "Your charm is magnetic, and romantic energy flows easily. If in a relationship, focus on compromise and shared joy. Singles might attract someone artistic or elegant.",
        "career": "Teamwork is key today. Offer help, collaborate, and build relationships at work. People are more likely to support your ideas when they feel heard.",
        "health": "Avoid emotional highs and lows. Ground yourself with calming activities like reading, music, or light movement like tai chi.",
        "money": "Splurging on something aesthetic is tempting—but make sure it’s within budget. A friend may offer useful financial advice—listen carefully.",
        "color": "Pink 🌸",
        "number": "8"
    },
    "scorpio": {
        "general": "Intensity surrounds you today, Scorpio. You may uncover hidden truths or feel a strong need to transform a part of your life. Trust your instincts, but avoid emotional power struggles. Use this energy for deep work, research, or emotional healing.",
        "love": "You crave depth and honesty. Relationships thrive when you're vulnerable. If single, someone mysterious may spark your curiosity—look beneath the surface.",
        "career": "This is a good day for strategic planning. Keep a close eye on competition and trust your gut when negotiating. A behind-the-scenes effort could bring major results.",
        "health": "Don’t let stress fester—talk it out or release it through intense physical activity like boxing or swimming.",
        "money": "You may discover a hidden expense or debt. Face it head-on and start resolving it. Avoid shady deals or get-rich-quick schemes.",
        "color": "Black ⚫",
        "number": "3"
    },
    "sagittarius": {
        "general": "Adventure calls, Sagittarius! You may feel restless or eager for new horizons. Whether it’s travel, a new hobby, or learning something fresh, feed your curiosity. Just don’t neglect responsibilities in the process—balance freedom with structure.",
        "love": "Honesty and laughter are your allies in love. Lighthearted conversations can deepen connections. If single, someone with a sense of humor and love for adventure may catch your eye.",
        "career": "Be bold with your ideas. Even if others hesitate, your vision can inspire change. Just remember to back up enthusiasm with facts.",
        "health": "Stay physically active—it’s your key to joy today. Try outdoor activities or group fitness for a motivational boost.",
        "money": "Impulse spending on experiences is likely—set a budget and stick to it. You might find a deal on a trip or class you've been eyeing.",
        "color": "Purple 🟣",
        "number": "7"
    },
    "capricorn": {
        "general": "Your discipline shines today, Capricorn. You’re in a mood to build something lasting—whether it’s a project, habit, or relationship. Just don’t let work consume your whole day; emotional fulfillment matters too.",
        "love": "You may feel reserved, but that doesn’t mean you're not interested. Show care through consistent actions. If single, someone older or more stable could catch your eye.",
        "career": "You’re laser-focused and ready to climb the ladder. Set new goals or outline your next steps—they’ll guide your productivity.",
        "health": "Watch for back or joint discomfort. Maintain good posture and take stretch breaks. A warm bath could do wonders.",
        "money": "It’s a great day for budgeting or starting long-term financial planning. You might consider investing or saving for something meaningful.",
        "color": "Navy Blue 🔵",
        "number": "10"
    },
    "aquarius": {
        "general": "You’re full of original ideas today, Aquarius. Let your imagination flow, but ground it with action. Connect with your community or like-minded people to spark new collaborations. Your insights could inspire real change.",
        "love": "You may seek intellectual stimulation in love. Conversations will deepen bonds. Someone quirky or different may attract you if you're single.",
        "career": "Think outside the box. A creative solution may set you apart at work. Avoid stubborn colleagues—focus on those open to change.",
        "health": "Your energy is vibrant but erratic. Meditation or breathing exercises can calm the mind. Eat brain-boosting foods like nuts and berries.",
        "money": "Today favors unconventional investments—research well before committing. Crowdfunding or joint ventures may be fruitful.",
        "color": "Turquoise 🟦",
        "number": "11"
    },
    "pisces": {
        "general": "Today is a dreamlike day for you, Pisces. You may feel more sensitive to others' moods and drawn to art, music, or poetry. Use your empathy for connection but set boundaries to protect your energy.",
        "love": "Romance thrives through tenderness and empathy. Create a cozy space to bond with your partner. If single, someone artistic or spiritual may surprise you.",
        "career": "Your intuition can help resolve a problem others missed. Trust your instincts, but confirm your findings. Ideal time for creative professions.",
        "health": "Get plenty of sleep and stay hydrated. Your body may feel sluggish if you ignore your limits. Light yoga or water therapy helps.",
        "money": "Avoid making financial decisions based on emotion. If in doubt, pause and ask a trusted advisor. Stick to needs, not wants.",
        "color": "Sea Green 🟩",
        "number": "12"
    }
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
    data = daily_horoscopes[zodiac]

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
    - 🌟 **Sun Sign (Zodiac)**: `{zodiac.title()}`
    - 💫 **Traits**: {zodiac_traits[zodiac]}
    """)
    
report = f"""
🪪 Daily Horoscope Report for {name}

🗓️ Date of Birth: {dob.strftime('%B %d, %Y')}
🌞 Zodiac Sign: {zodiac.title()}

🔮 Daily Horoscope:
{data['general']}

❤️ Love: {data['love']}
💼 Career: {data['career']}
🩺 Health: {data['health']}
🎨 Lucky Color: {data['color']}
🔢 Lucky Number: {data['number']}

💫 Traits of {zodiac.title()}:
{zodiac_traits[zodiac]}
"""
st.download_button(
    label="📄 Download Horoscope Report",
    data=report,
    file_name=f"{name}_horoscope_report.txt",
    mime="text/plain"
)

