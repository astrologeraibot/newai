import requests
import base64
from datetime import datetime

# 🔑 Enter your keys here
API_KEY = "4208ea20-bc34-4cc5-aa6b-9baa37463cb5"
API_SECRET = "Xx8wAbZRRrKbfjXQvASwy0go9kBbsI7lkWXVttYr"

# Get access token
def get_access_token():
    credentials = f"{API_KEY}:{API_SECRET}"
    encoded = base64.b64encode(credentials.encode()).decode()
    headers = {
        "Authorization": f"Basic {encoded}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    response = requests.post("https://api.prokerala.com/token", headers=headers, data={"grant_type": "client_credentials"})
    if response.status_code == 200:
        return response.json()["access_token"]
    return None

# Fetch birth chart
def get_prokerala_birth_chart(dob, tob, latitude, longitude):
    token = get_access_token()
    if not token:
        return {"error": "Authentication failed"}

    datetime_str = f"{dob}T{tob}"
    url = "https://api.prokerala.com/v2/astrology/birth-chart"
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "datetime": datetime_str,
        "latitude": latitude,
        "longitude": longitude,
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text}
