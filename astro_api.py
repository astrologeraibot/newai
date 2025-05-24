import requests

def get_daily_horoscope(sign):
    try:
        url = f"https://aztro.sameerkumar.website/?sign={sign.lower()}&day=today"
        response = requests.post(url)
        data = response.json()
        return data.get("description", "Could not fetch horoscope.")
    except Exception as e:
        return "Error fetching horoscope."

def get_birth_chart(name, dob, tob, place):
    return f"Birth chart for {name} born on {dob} at {tob} in {place}. (Simulated data)"
