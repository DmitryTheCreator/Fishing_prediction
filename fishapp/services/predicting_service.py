from ..serializers import PredictingSerializer
from typing import Optional
from ..models import Predicting
from .weather_service import WeatherService
from .order_service import OrderService
from .fish_service import FishService
from predicting.predicting import predicting
from datetime import date, timedelta

"""
    Данный модуль содержит программный слой с реализацией дополнительной бизнес-логики, 
    выполняемой перед или после выполнения операций над хранилищем данных (repository), 
    а также выполнение дополнительных операций над сериализаторами (если необходимо).

    ВАЖНО! Реализация данного слоя приведена в качестве демонстрации полной структуры RESTful веб-сервиса.
           В небольших проектах данный слой может быть избыточен, в таком случае, из контроллера ваших маршрутов 
           (Router в FastAPI или View в Django) можно напрямую работать с функциями хранилища данных (repository_service).
"""


class PredictingService:
    def get_predicting_by_id(self, id: int) -> Optional[PredictingSerializer]:
        result = Predicting.objects.filter(id=id).first()
        if result is not None:
            return PredictingSerializer(result)
        return result


    def get_all_predicitngs(self) -> PredictingSerializer:
        result = Predicting.objects.all()
        return PredictingSerializer(result, many=True)


    def get_all_predicitngs_by_date(self, date: str) -> PredictingSerializer:
        result = Predicting.objects.filter(date=date).all()
        return PredictingSerializer(result, many=True)


    def add_predicting(self, order_id: int) -> None:
        weather_service = WeatherService()
        order_service = OrderService()
        fish_service = FishService()

        # weather_service.delete_all_weather()
        # weather_service.add_weather_entry()

        day_1 = weather_service.get_all_weather_entries_by_date(date=date.today())
        day_2 = weather_service.get_all_weather_entries_by_date(date=date.today() + timedelta(days=1))
        day_3 = weather_service.get_all_weather_entries_by_date(date=date.today() + timedelta(days=2))
        days = [day_1, day_2, day_3]

        order = order_service.get_order_by_id(id=order_id)
        fish = fish_service.get_fish_by_id(id=order['kind_of_fish_id'].value)

        for day in days:
            for index in range(8):
                temperature_ovr = 1 - abs(fish['temperature'].value - day.data[index]['temperature']) / 100
                cloud_cover_ovr = 1 - abs(fish['cloud_cover'].value - day.data[index]['cloud_cover']) / 10
                precipitation_ovr = 1 - abs(fish['precipitation'].value - day.data[index]['precipitation']) / 10
                wind_speed_ovr = 1 - abs(fish['wind_speed'].value- day.data[index]['wind_speed']) / 100
                atmospheric_pressure_ovr = 1 - abs(fish['atmospheric_pressure'].value - day.data[index]['atmospheric_pressure']) / 100
                humidity_ovr = 1 - abs(fish['humidity'].value - day.data[index]['humidity']) / 4 / 100

                predicting_ratio = temperature_ovr * cloud_cover_ovr * precipitation_ovr * wind_speed_ovr * \
                                   atmospheric_pressure_ovr * humidity_ovr

                new_predicting = Predicting.objects.create(
                    order_id=order_id,
                    weather_condition_id=day.data[index]['id'],
                    predict=round(round(predicting_ratio, 2) * 100),
                    date=day.data[index]['date']
                )
                new_predicting.save()


    def update_predicting(self, predicting: PredictingSerializer, id: int) -> None:
        predicting_data = predicting.data
        predicting_gotten = Predicting.objects.filter(id=id).first()
        predicting_gotten.order_id = predicting_data.get('order_id')
        predicting_gotten.weather_condition_id = predicting_data.get('weather_condition_id')
        predicting_gotten.predict = predicting_data.get('predict')
        predicting_gotten.date = predicting_data.get('date')
        predicting_gotten.save()


    def delete_predicting_by_id(self, id: int) -> None:
        Predicting.objects.filter(id=id).first().delete()