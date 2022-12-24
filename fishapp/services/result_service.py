from ..serializers import ResultSerializer
from typing import Optional
from ..models import Result
from .fish_service import FishService
from .order_service import OrderService
from .predicting_service import PredictingService
from .employee_service import EmployeeService
from datetime import datetime, timedelta
import math

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
    
    
    def add_result(self, predicting_id: int, employee_id: int) -> None:
        fish_service = FishService()
        order_service = OrderService()
        predicting_service = PredictingService()
        employee_service = EmployeeService()

        predicting = predicting_service.get_predicting_by_id(id=predicting_id)
        order = order_service.get_order_by_id(id=predicting.data['order_id'])
        fish = fish_service.get_fish_by_id(id=order.data['kind_of_fish_id'])
        employee = employee_service.get_employee_by_id(id=employee_id)

        predicting_time = (fish.data['fishing_time'] * order.data['fish_amount']) / \
                          ((predicting.data['predict'] / 100) * (employee.data['performance'] / 100))

        new_result = Result.objects.create(
            order_id=order.data['id'],
            employee_id=employee_id,
            kind_of_fish_id=fish.data['id'],
            arrival_time=datetime.now().strftime('%Y-%m-%d %H:%M'),
            departure_time=(datetime.now() +
                            timedelta(hours=math.floor(predicting_time),
                                      minutes=round(predicting_time % 1, 2) % 60,
                                      seconds=0)).strftime('%Y-%m-%d %H:%M'),
            predict_time=f'{math.floor(predicting_time)}:{str(int(str(round(predicting_time % 1, 2)).split(".")[1]) % 60) if len(str(int(str(round(predicting_time % 1, 2)).split(".")[1]) % 60)) != 1 else "0" +  str(int(str(round(predicting_time % 1, 2)).split(".")[1]) % 60)}'
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
        result_gotten.predict_time = result_data.get('predict_time')
        result_gotten.save()


    def delete_result_by_id(self, id: int) -> None:
        Result.objects.filter(id=id).first().delete()