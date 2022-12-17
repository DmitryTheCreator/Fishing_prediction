from ..serializers import FishSerializer
from typing import Optional
from ..models import KindOfFish

"""
    Данный модуль содержит программный слой с реализацией дополнительной бизнес-логики, 
    выполняемой перед или после выполнения операций над хранилищем данных (repository), 
    а также выполнение дополнительных операций над сериализаторами (если необходимо).
    ВАЖНО! Реализация данного слоя приведена в качестве демонстрации полной структуры RESTful веб-сервиса.
           В небольших проектах данный слой может быть избыточен, в таком случае, из контроллера ваших маршрутов 
           (Router в FastAPI или View в Django) можно напрямую работать с функциями хранилища данных (repository_service).
"""

class FishService:
    def get_fish_by_id(self, id: int) -> Optional[FishSerializer]:
        result = KindOfFish.objects.filter(id=id).first()
        if result is not None:
            return FishSerializer(result)
        return result


    def get_fish_by_name(self, fish_name: str) -> FishSerializer:
        result = KindOfFish.objects.filter(name=fish_name.lower()).first()
        return FishSerializer(result)


    def get_all_fish(self) -> FishSerializer:
        result = KindOfFish.objects.all()
        return FishSerializer(result, many=True)


    def add_fish(self, fish: FishSerializer) -> None:
        fish_data = fish.data
        new_fish = KindOfFish.objects.create(
            name=fish_data.get('name'),
            temperature=fish_data.get('temperature'),
            cloud_cover=fish_data.get('cloud_cover'),
            precipitation=fish_data.get('precipitation'),
            wind_speed=fish_data.get('wind_speed'),
            atmospheric_pressure=fish_data.get('atmospheric_pressure'),
            humidity=fish_data.get('humidity')
        )
        new_fish.save()


    def update_fish_info_by_id(self, fish: FishSerializer, id: int) -> None:
        fish_data = fish.data
        fish_gotten = KindOfFish.objects.filter(id=id).first()
        fish_gotten.name = fish_data.get('name')
        fish_gotten.temperature = fish_data.get('temperature')
        fish_gotten.cloud_cover = fish_data.get('cloud_cover')
        fish_gotten.precipitation = fish_data.get('precipitation')
        fish_gotten.wind_speed = fish_data.get('wind_speed')
        fish_gotten.atmospheric_pressure = fish_data.get('atmospheric_pressure')
        fish_gotten.humidity = fish_data.get('humidity')
        fish_gotten.save()


    def update_fish_info_by_name(self, fish: FishSerializer) -> None:
        fish_data = fish.data
        fish_gotten = KindOfFish.objects.filter(name=fish_data.get('name').lower()).first()
        fish_gotten.temperature = fish_data.get('temperature')
        fish_gotten.cloud_cover = fish_data.get('cloud_cover')
        fish_gotten.precipitation = fish_data.get('precipitation')
        fish_gotten.wind_speed = fish_data.get('wind_speed')
        fish_gotten.atmospheric_pressure = fish_data.get('atmospheric_pressure')
        fish_gotten.humidity = fish_data.get('humidity')
        fish_gotten.save()


    def delete_fish_by_id(self, id: int) -> None:
        KindOfFish.objects.filter(id=id).delete()


    def delete_fish_by_name(self, fish_name: str) -> None:
        KindOfFish.objects.filter(name=fish_name.lower()).first().delete()

