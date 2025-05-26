import requests

def get_daily_horoscope(sign):
    """Fetch daily horoscope using the free Aztro API."""
    url = f"https://aztro.sameerkumar.website/?sign={sign.lower()}&day=today"
    response = requests.post(url)
    if response.status_code == 200:
        data = response.json()
        return f"""
**Horoscope**: {data['description']}

- 💖 **Compatibility**: {data['compatibility']}
- 💡 **Mood**: {data['mood']}
- 🔢 **Lucky Number**: {data['lucky_number']}
- 🕰️ **Lucky Time**: {data['lucky_time']}
"""
    else:
        return "Sorry, couldn't fetch horoscope right now. Try again later."

def get_birth_chart(name, dob, tob, place):
    """Stub function — replace with real logic or API if needed."""
    return f"""
Name: {name}
Date of Birth: {dob}
Time of Birth: {tob}
Place of Birth: {place}

(For detailed birth charts, connect to an astrology API like AstroSeek or Swiss Ephemeris.)
"""
