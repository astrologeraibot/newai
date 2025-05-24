import requests

def get_daily_horoscope(sign):
    try:
        url = f"https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily?sign={sign.lower()}"
        response = requests.get(url)
        data = response.json()
        horoscope = data.get("horoscope") or data.get("data", {}).get("horoscope")
        return horoscope or "No daily horoscope available."
    except Exception as e:
        return f"Error fetching horoscope: {str(e)}"

def get_birth_chart(name, dob, tob, place):
    return (
        f"{name}, born on {dob} at {tob} in {place}, your Sun sign is a key influence. "
        "You are naturally drawn to growth, intuition, and personal transformation."
    )
