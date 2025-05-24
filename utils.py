predefined_questions = [
    "What does my birth chart say about me?",
    "Can you analyze my love life through astrology?",
    "Tell me about my career prospects astrologically.",
    "Can you describe my main weaknesses?"
]

def get_answer(query, sign):
    if "love" in query.lower():
        return f"As a {sign}, you seek deep emotional connections and loyalty in love."
    elif "career" in query.lower():
        return f"Your career path is influenced by your ambition and your {sign} sign's strength."
    elif "weakness" in query.lower():
        return f"Your main astrological weakness might be stubbornness, which is common for {sign}s."
    else:
        return f"As a {sign}, the stars suggest a balanced but reflective period ahead."
