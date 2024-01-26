from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = '7c6e47ff49bfc609ca2f7e0192558b35'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
FORECAST_URL = 'http://api.openweathermap.org/data/2.5/forecast'

def get_weather_data(city):
    params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data

def get_forecast_data(city):
    params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
    response = requests.get(FORECAST_URL, params=params)
    data = response.json()
    return data['list']

def translate_condition(condition):
    translations = {
        'Clear': 'Céu limpo',
        'Clouds': 'Nuvens',
        'Rain': 'Chuva',
        'Snow': 'Neve',
        'Thunderstorm': 'Tempestade',
        'Mist': 'Névoa',
        'Fog': 'Nevoeiro'
    }
    return translations.get(condition, condition)

@app.route('/', methods=['GET', 'POST'])
def index():
    city = request.form.get('city') or 'London'  # Default city is London
    weather_data = get_weather_data(city)
    forecast_data = get_forecast_data(city)
    return render_template('index.html', city=city, weather_data=weather_data, forecast_data=forecast_data, translate_condition=translate_condition)

if __name__ == '__main__':
    app.run(debug=True)
