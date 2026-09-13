import requests 
print("===== WEATHER APP =====") 
latitude = float(input("Enter latitude: ")) 
longitude = float(input("Enter longitude: ")) 
url = "https://api.open-meteo.com/v1/forecast" 
params = {    
    "latitude": latitude,    
    "longitude": longitude,    
    "current": "temperature_2m,relative_humidity_2m,wind_speed_10m" } 
response = requests.get(url, params=params, timeout=10) 
if response.status_code == 200:    
    data = response.json()    
    temperature = data["current"]["temperature_2m"]   
    humidity = data["current"]["relative_humidity_2m"]    
    wind = data["current"]["wind_speed_10m"]   
    print("\n===== CURRENT WEATHER =====")    
    print("Temperature:", temperature, "C")   
    print("Humidity:", humidity, "%")    
    print("Wind Speed:", wind, "km/h") 
else:    
    print("Unable to get weather data.")