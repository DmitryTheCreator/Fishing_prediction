import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_data(url_day: str = ''):
    headers = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/105.0.0.0 Safari/537.36 '
    }
    url = f'https://www.gismeteo.ru/weather-ufa-4588/{url_day}'

    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    date, time, weather_conditions, temperature, wind_speed, atmospheric_pressure, humidity = '', [], [], [], [], [], []
    
    date = str(datetime.now().date())

    time_soup = soup.find('div', class_='widget-row widget-row-time').find_all('div', class_='row-item')
    for item in time_soup:
        hours = item.text[:-2]
        minutes = item.find(class_='time-sup').text
        time.append(f'{hours}:{minutes}')

    weather_conditions_soup = soup.find('div', class_='widget-row widget-row-icon').find_all('div', class_='row-item')
    for item in weather_conditions_soup:
        weather_conditions.append(item.find('div', {'data-text': True})['data-text'])

    temperature_soup = soup.find('div', class_='widget-row-chart widget-row-chart-temperature')\
        .find('div', class_='values').find_all('span', class_='unit unit_temperature_c')
    for item in temperature_soup:
        temperature.append(item.text)

    wind_speed_soup = soup.find('div', class_='widget-row widget-row-wind-speed-gust row-with-caption') \
        .find_all('div', class_='row-item')
    for item in wind_speed_soup:
        wind_speed.append(item.find('span').text[:-1])

    atmospheric_pressure_soup = soup.find('div', class_='widget-row-chart widget-row-chart-pressure') \
        .find('div', class_='chart').find('div', class_='values').find_all('div', class_='value')
    for item in atmospheric_pressure_soup:
        atmospheric_pressure.append(item.find('span', class_='unit unit_pressure_mm_hg_atm').text)

    humidity_soup = soup.find('div', class_='widget-row widget-row-humidity')
    for item in humidity_soup:
        humidity.append(item.text)

    return temperature, weather_conditions, wind_speed, atmospheric_pressure, humidity, date, time
