from ..serializers import ResultSerializer
from .repository_service import *
from ..models import Result

"""
    Данный модуль содержит программный слой с реализацией дополнительной бизнес-логики, 
    выполняемой перед или после выполнения операций над хранилищем данных (repository), 
    а также выполнение дополнительных операций над сериализаторами (если необходимо).

    ВАЖНО! Реализация данного слоя приведена в качестве демонстрации полной структуры RESTful веб-сервиса.
           В небольших проектах данный слой может быть избыточен, в таком случае, из контроллера ваших маршрутов 
           (Router в FastAPI или View в Django) можно напрямую работать с функциями хранилища данных (repository_service).
"""


class ResultService:
    def get_result_by_id(self, id: int) -> Optional[ResultSerializer]:
        result = Result.objects.filter(id=id).first()
        if result is not None:
            return ResultSerializer(result)
        return result

    def add_result(self, result: ResultSerializer) -> None:
        result_data = result.data  # получаем валидированные с помощью сериализатора данные (метод .data  возвращает объект типа dict)
        new_result = Result.objects.create(
            order=result_data.get('order'),
            employee=result_data.get('employee'),
            kind_of_fish=result_data.get('kind_of_fish'),
            arrival_time=result_data.get('arrival_time'),
            departure_time=result_data.get('departure_time')
        )
        new_result.save()

    def update_result(self, result: ResultSerializer) -> None:
        result_data = result.data
        result_gotten = Result.objects.filter(id=result_data.get('id'))
        result_gotten.order = result_data.get('order')
        result_gotten.employee = result_data.get('employee')
        result_gotten.kind_of_fish = result_data.get('kind_of_fish')
        result_gotten.arrival_time = result_data.get('arrival_time')
        result_gotten.departure_time = result_data.get('departure_time')
        result_gotten.save()


    def delete_result_by_id(self, id: int) -> None:
        Result.objects.filter(id=id).first().delete()