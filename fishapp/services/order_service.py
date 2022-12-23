from ..serializers import OrderSerializer
from typing import Optional
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


    def get_all_orders(self) -> OrderSerializer:
        result = Order.objects.all()
        return OrderSerializer(result, many=True)


    def create_order(self, order: OrderSerializer) -> None:
        order_data = order.data
        new_order = Order.objects.create(
            customer_name=order_data.get('customer_name'),
            deadline=order_data.get('deadline'),
            receiving_time=order_data.get('receiving_time'),
            kind_of_fish_id=order_data.get('kind_of_fish_id'),
            fish_amount=order_data.get('fish_amount'),
            in_progress=order_data.get('in_progress')
        )
        new_order.save()


    def update_order(self, order: OrderSerializer, id: int) -> None:
        order_data = order.data
        order_gotten = Order.objects.filter(id=id).first()
        order_gotten.customer_name = order_data.get('customer_name')
        order_gotten.deadline = order_data.get('deadline')
        order_gotten.receiving_time = order_data.get('receiving_time')
        order_gotten.kind_of_fish_id = order_data.get('kind_of_fish_id')
        order_gotten.fish_amount = order_data.get('fish_amount')
        order_gotten.in_progress = order_data.get('in_progress')
        order_gotten.save()


    def delete_order_by_id(self, id: int) -> None:
        Order.objects.filter(id=id).first().delete()