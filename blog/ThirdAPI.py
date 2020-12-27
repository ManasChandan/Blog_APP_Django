import requests , json

class Weather():
    api_key = ''
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    def CityWeather(self , city='Delhi'):
        complete_url = self.base_url + "appid=" + self.api_key + "&q=" + city
        response = requests.get(complete_url)
        x = response.json() 
        if x["cod"] != "404":
            y = x["main"] 
            current_temperature = y["temp"] - 273.15
            current_pressure = y["pressure"] 
            current_humidiy = y["humidity"] 
            z = x["weather"] 
            weather_description = z[0]["description"]
            values = {'temp' : round(current_temperature,2) , 'pre' : current_pressure , 'humid' : current_humidiy , 'city' : city , 'desp' : weather_description}
            return values
