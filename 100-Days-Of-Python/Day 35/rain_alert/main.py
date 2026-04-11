# could not find a free weather api that did not require a credit card, 
# so I used the one from the course

import requests


# https://api.openweathermap.org/data/2.5/weather?lat=49.934530&lon=11.583753&appid=4310c61766f88c7de6e90aa98e8272d8

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather?"
api_key = "4310c61766f88c7de6e90aa98e8272d8"

weather_params = {
    "lat": 49.934530,
    "lon": 11.583753,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
print(response.json())

# weather_data = reaponse.json()
# weather_slice = weather_data["list"][:12]

# will_rain = False
# for hour_data in weather_slice:
#     condition_code = hour_data["weather"][0]["id"]
#     if int(condition_code) < 700:
#         will_rain = True
#     if will_rain:
#         print("Bring an umbrella.")

