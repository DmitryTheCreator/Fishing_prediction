from ..serializers import WeatherSerializer
from typing import Optional
from ..models import WeatherCondition
from scrapping.run import get_data
from datetime import date, timedelta

"""
    Данный модуль содержит программный слой с реализацией дополнительной бизнес-логики, 
    выполняемой перед или после выполнения операций над хранилищем данных (repository), 
    а также выполнение дополнительных операций над сериализаторами (если необходимо).

    ВАЖНО! Реализация данного слоя приведена в качестве демонстрации полной структуры RESTful веб-сервиса.
           В небольших проектах данный слой может быть избыточен, в таком случае, из контроллера ваших маршрутов 
           (Router в FastAPI или View в Django) можно напрямую работать с функциями хранилища данных (repository_service).
"""


class WeatherService:
    def get_weather_entry_by_id(self, id: int) -> Optional[WeatherSerializer]:
        result = WeatherCondition.objects.filter(id=id).first()
        if result is not None:
            return WeatherSerializer(result)
        return result


    def get_all_weather_entries(self) -> WeatherSerializer:
        result = WeatherCondition.objects.all()
        return WeatherSerializer(result, many=True)


    def get_all_weather_entries_by_date(self, date: str) -> WeatherSerializer:
        result = WeatherCondition.objects.filter(date=date).all()
        return WeatherSerializer(result, many=True)


    # def add_weather_entry(self, weather: WeatherSerializer) -> None:
    #     weather_data = weather.data  # получаем валидированные с помощью сериализатора данные (метод .data  возвращает объект типа dict)
    #     new_weather = WeatherCondition.objects.create(
    #         temperature=weather_data.get('temperature'),
    #         cloud_cover=weather_data.get('cloud_cover'),
    #         precipitation=weather_data.get('precipitation'),
    #         wind_speed=weather_data.get('wind_speed'),
    #         atmospheric_pressure=weather_data.get('atmospheric_pressure'),
    #         humidity=weather_data.get('humidity'),
    #         date=weather_data.get('date'),
    #         time=weather_data.get('time'),
    #     )
    #     new_weather.save()

    def add_weather_entry(self, weather: WeatherSerializer = None) -> None:

        days = ['today/', 'tomorrow/', '3-day/']
        for day in days:
            temperature, weather_cond, wind_speed_range, atmospheric_pressure, humidity, date_, time = get_data(
                url_day=day)


            for index in range(len(temperature)):
                if ',' in weather_cond[index]:
                    cloud_cover = weather_cond[index].split()[0][:-1]
                    precipitation = weather_cond[index].split(',')[-1].split()[0]
                else:
                    cloud_cover = weather_cond[index].split()[0]
                    precipitation = 'нет'

                wind_speed_average = 0
                if '-' in wind_speed_range[index]:
                    wind_speed_average = int(wind_speed_range[index].split('-')[-1]) - int(
                        wind_speed_range[index].split('-')[0])
                else:
                    wind_speed_average = int(wind_speed_range[index])

                kind_of_cloud_cover = ['ясно', 'малооблачно', 'облачно', 'пасмурно', 'гроза']
                cloud_cover_index_weather = kind_of_cloud_cover.index(cloud_cover.lower())

                kind_of_precipitation = ['нет', 'небольшой', '-', 'сильный']

                if precipitation.lower() in kind_of_precipitation:
                    precipitation_index_weather = kind_of_precipitation.index(precipitation.lower())
                else:
                    precipitation_index_weather = 0

                if not temperature[index].isdigit():
                    temp = 0 - int(temperature[index][1:])
                else:
                    temp = int(temperature[index])

                new_weather = WeatherCondition.objects.create(
                    temperature=temp,
                    cloud_cover=cloud_cover_index_weather,
                    precipitation=precipitation_index_weather,
                    wind_speed=wind_speed_average,
                    atmospheric_pressure=atmospheric_pressure[index],
                    humidity=humidity[index],
                    date=str(date.today() + timedelta(days=days.index(day))),
                    time=time[index]
                )
                new_weather.save()


    def delete_all_weather_entries_by_date(self, date: str) -> None:
        WeatherCondition.objects.filter(date=date).all().delete()


    def delete_weather_entry_by_id(self, id: int) -> None:
        WeatherCondition.objects.filter(id=id).first().delete()


    def delete_all_weather(self) -> None:
        WeatherCondition.objects.all().delete()
