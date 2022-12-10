from ..serializers import WeatherSerializer
from typing import Optional
from ..models import WeatherCondition

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


    def add_weather_entry(self, weather: WeatherSerializer) -> None:
        weather_data = weather.data  # получаем валидированные с помощью сериализатора данные (метод .data  возвращает объект типа dict)
        new_weather = WeatherCondition.objects.create(
            temperature=weather_data.get('temperature'),
            cloud_cover=weather_data.get('cloud_cover'),
            precipitation=weather_data.get('precipitation'),
            wind_speed=weather_data.get('wind_speed'),
            atmospheric_pressure=weather_data.get('atmospheric_pressure'),
            humidity=weather_data.get('humidity'),
            date=weather_data.get('date'),
            time=weather_data.get('time'),
        )
        new_weather.save()


    def delete_all_weather_entries_by_date(self, date: str) -> None:
        WeatherCondition.objects.filter(date=date).all().delete()


    def delete_weather_entry_by_id(self, id: int) -> None:
        WeatherCondition.objects.filter(id=id).first().delete()
