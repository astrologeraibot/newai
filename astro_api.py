import requests

def get_daily_horoscope(sign):
    url = f"https://aztro.sameerkumar.website/?sign={sign.lower()}&day=today"
    response = requests.post(url)
    if response.status_code == 200:
        data = response.json()
        return f"""
**Horoscope**: {data['description']}

- 💖 Compatibility: {data['compatibility']}
- 💡 Mood: {data['mood']}
- 🔢 Lucky Number: {data['lucky_number']}
- 🕰️ Lucky Time: {data['lucky_time']}
"""
    return "Could not fetch horoscope."
