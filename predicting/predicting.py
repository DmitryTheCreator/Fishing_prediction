from scrapping.run import get_data
from fishapp.models import WeatherCondition
import requests


def predicting(order_id: int, url_day: str = ''):
    temperature, weather_cond, wind_speed_range, atmospheric_pressure, humidity, date, time = get_data(url_day=url_day)
    cloud_cover, precipitation = '', ''

    headers = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/105.0.0.0 Safari/537.36 '
    }
    url = f'http://127.0.0.1:8000/fishzone/order/{order_id}'

    fish_id = requests.get(url=url, headers=headers).text['kind_of_fish_id']
    fish = requests.get(url=f'http://127.0.0.1:8000/fishzone/fish/{fish_id}', headers=headers).text


    predicting_ratios = []
    for ind in range(len(temperature)):
        if ',' in weather_cond[ind]:
            cloud_cover = weather_cond[ind].split()[0][:-1]
            precipitation = weather_cond[ind].split(',')[-1].split()[0]
        else:
            cloud_cover = weather_cond[ind].split()[0]
            precipitation = 'нет'

        wind_speed_average = 0
        if '-' in wind_speed_range:
            wind_speed_average = int(wind_speed_range[ind].split('-')[-1]) - int(wind_speed_range[ind].split('-')[0])
        else:
            wind_speed_average = int(wind_speed_range[ind])

        for index in range(len(temperature)):
            new_weather = WeatherCondition.objects.create(
                temperature=temperature[index],
                cloud_cover=cloud_cover[index],
                precipitation=precipitation[index],
                wind_speed=wind_speed_average[index],
                atmospheric_pressure=atmospheric_pressure[index],
                humidity=humidity[index],
                date=date,
                time=time[index]
            )
            new_weather.save()

        weather = {
            'temperature': temperature[ind],
            'cloud_cover': cloud_cover,
            'precipitation': precipitation,
            'wind_speed': wind_speed_average,
            'atmospheric_pressure':  int(atmospheric_pressure[ind]),
            'humidity': int(humidity[ind])
        }

        if '−' in weather.temperature:
            temperature_ovr = 1 - abs(fish['temperature'] - int(weather['temperature'][1:])) / 100
        else:
            temperature_ovr = 1 - abs(fish['temperature'] - int(weather['temperature'])) / 100

        kind_of_cloud_cover = ['ясно', 'малооблачно', 'облачно', 'пасмурно', 'гроза']
        cloud_cover_index_fish = kind_of_cloud_cover.index(fish['cloud_cover'].lower())
        cloud_cover_index_weather = kind_of_cloud_cover.index(weather['cloud_cover'].lower())
        cloud_cover_ovr = 1 - abs(cloud_cover_index_fish - cloud_cover_index_weather) / 10

        kind_of_precipitation = ['нет', 'небольшой', '-', 'сильный']
        precipitation_index_fish, precipitation_index_weather = 2, 2
        for precipitation in kind_of_precipitation:
            if precipitation in fish['precipitation'].lower():
                precipitation_index_fish = kind_of_precipitation.index(precipitation)
            if precipitation in weather['precipitation'].lower():
                precipitation_index_weather = kind_of_precipitation.index(precipitation)

        precipitation_ovr = 1 - abs(precipitation_index_fish - precipitation_index_weather) / 10
        wind_speed_ovr = 1 - abs(fish['wind_speed'] - weather['wind_speed']) / 100
        atmospheric_pressure_ovr = 1 - abs(weather['atmospheric_pressure'] - 760) / 100
        humidity_ovr = 1 - abs(fish['humidity'] - weather['humidity']) / 4 / 100

        predicting_ratio = temperature_ovr * cloud_cover_ovr * precipitation_ovr * wind_speed_ovr * \
                           atmospheric_pressure_ovr * humidity_ovr
        predicting_ratios.append(round(round(predicting_ratio, 2) * 100))
    return predicting_ratios
    # return {
    #     'date': f'{date}',
    #     'weather': [
    #         {
    #             'time': f'{time[0]}',
    #             'temperature': f'{temperature[0]}',
    #             'cloud_cover': f'{weather_cond[0].split()[0][:-1]}',
    #             'precipitation': f'{weather_cond[0].split(",")[-1]}',
    #             'predict': f'{predicting_ratios[0]}'
    #         },
    #         {
    #             'time': f'{time[1]}',
    #             'temperature': f'{temperature[1]}',
    #             'cloud_cover': f'{weather_cond[1].split()[0][:-1]}',
    #             'precipitation': f'{weather_cond[1].split(",")[-1]}',
    #             'predict': f'{predicting_ratios[1]}'
    #         },
    #         {
    #             'time': f'{time[2]}',
    #             'temperature': f'{temperature[2]}',
    #             'cloud_cover': f'{weather_cond[2].split()[0][:-1]}',
    #             'precipitation': f'{weather_cond[2].split(",")[-1]}',
    #             'predict': f'{predicting_ratios[2]}'
    #         },
    #         {
    #             'time': f'{time[3]}',
    #             'temperature': f'{temperature[3]}',
    #             'cloud_cover': f'{weather_cond[3].split()[0][:-1]}',
    #             'precipitation': f'{weather_cond[3].split(",")[-1]}',
    #             'predict': f'{predicting_ratios[3]}'
    #         },
    #         {
    #             'time': f'{time[4]}',
    #             'temperature': f'{temperature[4]}',
    #             'cloud_cover': f'{weather_cond[4].split()[0][:-1]}',
    #             'precipitation': f'{weather_cond[4].split(",")[-1]}',
    #             'predict': f'{predicting_ratios[4]}'
    #         },
    #         {
    #             'time': f'{time[5]}',
    #             'temperature': f'{temperature[5]}',
    #             'cloud_cover': f'{weather_cond[5].split()[0][:-1]}',
    #             'precipitation': f'{weather_cond[5].split(",")[-1]}',
    #             'predict': f'{predicting_ratios[5]}'
    #         },{
    #             'time': f'{time[6]}',
    #             'temperature': f'{temperature[6]}',
    #             'cloud_cover': f'{weather_cond[6].split()[0][:-1]}',
    #             'precipitation': f'{weather_cond[6].split(",")[-1]}',
    #             'predict': f'{predicting_ratios[6]}'
    #         },
    #         {
    #             'time': f'{time[7]}',
    #             'temperature': f'{temperature[7]}',
    #             'cloud_cover': f'{weather_cond[7].split()[0][:-1]}',
    #             'precipitation': f'{weather_cond[7].split(",")[-1]}',
    #             'predict': f'{predicting_ratios[7]}'
    #         },
    #     ]
    # }

