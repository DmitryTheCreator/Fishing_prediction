from ..serializers import ResultSerializer
from typing import Optional
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


    def get_all_results(self) -> ResultSerializer:
        result = Result.objects.all()
        return ResultSerializer(result, many=True)
    
    
    def add_result(self, result: ResultSerializer) -> None:
        result_data = result.data  # получаем валидированные с помощью сериализатора данные (метод .data  возвращает объект типа dict)
        new_result = Result.objects.create(
            order_id=result_data.get('order_id'),
            employee_id=result_data.get('employee_id'),
            kind_of_fish_id=result_data.get('kind_of_fish_id'),
            arrival_time=result_data.get('arrival_time'),
            departure_time=result_data.get('departure_time')
        )
        new_result.save()


    def update_result(self, result: ResultSerializer, id: int) -> None:
        result_data = result.data
        result_gotten = Result.objects.filter(id=id).first()
        result_gotten.order_id = result_data.get('order_id')
        result_gotten.employee_id = result_data.get('employee_id')
        result_gotten.kind_of_fish_id = result_data.get('kind_of_fish_id')
        result_gotten.arrival_time = result_data.get('arrival_time')
        result_gotten.departure_time = result_data.get('departure_time')
        result_gotten.save()


    def delete_result_by_id(self, id: int) -> None:
        Result.objects.filter(id=id).first().delete()