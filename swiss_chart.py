import swisseph as swe

def get_planet_positions(dob, tob):
    jd = swe.julday(dob.year, dob.month, dob.day, tob.hour + tob.minute / 60.0)
    planets = ['Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn']
    positions = {}
    for i, name in enumerate(planets):
        lon, lat, dist = swe.calc_ut(jd, i)
        positions[name] = f"{lon:.2f}°"
    return positions
