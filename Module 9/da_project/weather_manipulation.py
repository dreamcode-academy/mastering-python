import pandas as pd
import sqlite3
import re

def extract_temperature(text):
    match = re.search(r'(\d+)', text)
    return int(match.group()) if match else None


def extract_wind_speed(text):
    match = re.search(r'(\d+) mph', text)
    return int(match.group(1) if match else None)

df = pd.read_json("Miami_DetailedWeatherData.json")

df["Temperature"] = df['Detailed Forecast'].apply(extract_temperature)
df['Wind Speed'] = df['Detailed Forecast'].apply(extract_wind_speed)

df['Time of Day'] = df['Period'].apply(lambda x: 'Night' if 'Nighr' in x else 'Day')

conn = sqlite3.connect('weather_data.db')

df.to_sql('weather_forecast', conn, if_exists='replace', index=False)

conn.close()
