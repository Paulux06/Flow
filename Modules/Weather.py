import requests

class Weather:
    def Temperature(self, city):
        self.weather = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+',fr&APPID=3a87a97e8c462b3ad86e7716af734b03').json()

        if not self.weather == {'cod': '404', 'message': 'city not found'}:
            return round(self.weather['main']['temp'] - 273.15, 1)
        else:
            return False

    def TypeTemp(self, city):
        self.weather = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+',fr&APPID=3a87a97e8c462b3ad86e7716af734b03').json()

        if not self.weather == {'cod': '404', 'message': 'city not found'}:
            Temp = False
            if self.weather['weather'][0]['main'] == 'Clear':
                Temp = 'un ciel clair'
            if self.weather['weather'][0]['main'] == 'Clouds':
                Temp = 'un ciel nuageux'
            if self.weather['weather'][0]['main'] == 'Snow':
                Temp = 'de la neige'
            if self.weather['weather'][0]['main'] == 'Drizzle':
                Temp = 'du brouillard'
            if self.weather['weather'][0]['main'] == 'Thunderstorm':
                Temp = 'des éclairs'
            if self.weather['weather'][0]['main'] == 'Rain':
                Temp = 'de la pluie'
            return Temp
        else:
            return False 