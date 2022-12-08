from ..serializers import PredictingSerializer
from .repository_service import *
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

    def add_predicting(self, result: PredictingSerializer) -> None:
        predicting_data = predicting.data  # получаем валидированные с помощью сериализатора данные (метод .data  возвращает объект типа dict)
        new_predicting = Predicitng.objects.create(
            kind_of_fish=predicting_data.get('kind_of_fish'),
            weather_condition=predicting_data.get('weather_condition')
        )
        new_predicting.save()


    def update_predicting(self, predicting: PredictingSerializer) -> None:
        predicting_data = predicting.data
        predicting_gotten = Predicting.objects.filter(id=predicting_data.get('id'))
        predicting_gotten.kind_of_fish = predicting_data.get('kind_of_fish')
        predicting_gotten.weather_condition = predicting_data.get('weather_condition')
        predicting_gotten.save()


    def delete_result_by_id(self, id: int) -> None:
        Predicting.objects.filter(id=id).first().delete()