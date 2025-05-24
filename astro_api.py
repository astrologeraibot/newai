import requests

def get_daily_horoscope(sign):
    try:
        url = f"https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily?sign={sign.lower()}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        horoscope = data.get("horoscope") or data.get("data", {}).get("horoscope")
        return horoscope or "No daily horoscope available for today."
    except Exception as e:
        return f"Error fetching horoscope: {str(e)}"

def get_birth_chart(name, dob, tob, place):
    return f"Simulated birth chart for {name} born on {dob} at {tob} in {place}."
