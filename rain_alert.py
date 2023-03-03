import requests
Api_key="2775d2b53613ac93d311e76c0d54abf3"
MY_LAT=22.572645
MY_LONG=88.363892
parameters={
    # ?lat={lat}&lon={lon}&exclude={part}&appid={API key}"
    "lat":MY_LAT,
    "lon":MY_LONG,
    "appid":Api_key,
    "exclude":"current,minutely,daily"
}
response=requests.get(url="https://api.openweathermap.org/data/2.5/onecall",params=parameters)
response.raise_for_status()
data=response.json()
weather_Slice=data["hourly"][:12]
# print(weather_Slice)
WILL_RAIN=False
for hour_data in weather_Slice:
    codition_code=(hour_data["weather"][0]["id"])
    if int(codition_code)<700:
        WILL_RAIN=True


if WILL_RAIN==True:
     print("BRING AN UMBRELLA")
else:
    print("No Need ")



# print(data["hourly"][0]["weather"][0]["id"])
