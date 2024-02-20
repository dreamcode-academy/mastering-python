import requests
from bs4 import BeautifulSoup
import pandas as pd
import json



url = "https://forecast.weather.gov/MapClick.php?lat=25.7748&lon=-80.1977"

r = requests.get(url, timeout=10)

soup = BeautifulSoup(r.content, "html.parser")

forecast_body = soup.find('div', id="detailed-forecast-body")
forecast_rows = forecast_body.find_all('div', class_="row-forecast")

forecast_periods = [row.find(class_ = "forecast-label").get_text().strip() for row in forecast_rows]
detailed_forecasts = [row.find(class_ = "forecast-text").get_text().strip() for row in forecast_rows]



df = pd.DataFrame({
    "Period": forecast_periods,
    "Detailed Forecast": detailed_forecasts
})

#df.to_csv("Miami_DetailedWeatherData.csv")

json_data = df.to_json(orient='records')

with open("Miami_DetailedWeatherData.json", "w") as json_file:
    json_file.write(json_data)