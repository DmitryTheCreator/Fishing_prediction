from ..serializers import OrderSerializer
from .repository_service import *
from ..models import Order

"""
    Данный модуль содержит программный слой с реализацией дополнительной бизнес-логики, 
    выполняемой перед или после выполнения операций над хранилищем данных (repository), 
    а также выполнение дополнительных операций над сериализаторами (если необходимо).

    ВАЖНО! Реализация данного слоя приведена в качестве демонстрации полной структуры RESTful веб-сервиса.
           В небольших проектах данный слой может быть избыточен, в таком случае, из контроллера ваших маршрутов 
           (Router в FastAPI или View в Django) можно напрямую работать с функциями хранилища данных (repository_service).
"""


class OrderService:
    def get_order_by_id(self, id: int) -> Optional[OrderSerializer]:
        result = Order.objects.filter(id=id).first()
        if result is not None:
            return OrderSerializer(result)
        return result

    def create_order(self, order: OrderSerializer) -> None:
        order_data = order.data  # получаем валидированные с помощью сериализатора данные (метод .data  возвращает объект типа dict)
        new_order = Order.objects.create(
            customer_name=order_data.get('name'),
            deadline=order_data.get('deadline'),
            receiving_time=order_data.get('receiving_time'),
            fish_name=order_data.get('fish_name'),
            fish_amount=order_data.get('fish_amount'),
            in_progress=order_data.get('in_progress')
        )
        new_order.save()

    def delete_order_by_id(self, id: str) -> None:
        Order.objects.filter(id=id).first().delete()