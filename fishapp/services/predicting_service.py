from ..serializers import PredictingSerializer
from typing import Optional
from ..models import Predicting

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


    def add_predicting(self, predicting: PredictingSerializer) -> None:
        predicting_data = predicting.data 
        new_predicting = Predicting.objects.create(
            kind_of_fish_id=predicting_data.get('kind_of_fish_id'),
            weather_condition_id=predicting_data.get('weather_condition_id')
        )
        new_predicting.save()


    def update_predicting(self, predicting: PredictingSerializer, id: int) -> None:
        predicting_data = predicting.data
        predicting_gotten = Predicting.objects.filter(id=id).first()
        predicting_gotten.kind_of_fish_id = predicting_data.get('kind_of_fish_id')
        predicting_gotten.weather_condition_id = predicting_data.get('weather_condition_id')
        predicting_gotten.save()


    def delete_predicting_by_id(self, id: int) -> None:
        Predicting.objects.filter(id=id).first().delete()