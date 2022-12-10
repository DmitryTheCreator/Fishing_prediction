from ..serializers import EmployeeSerializer
from typing import Optional
from ..models import Employee

"""
    Данный модуль содержит программный слой с реализацией дополнительной бизнес-логики, 
    выполняемой перед или после выполнения операций над хранилищем данных (repository), 
    а также выполнение дополнительных операций над сериализаторами (если необходимо).

    ВАЖНО! Реализация данного слоя приведена в качестве демонстрации полной структуры RESTful веб-сервиса.
           В небольших проектах данный слой может быть избыточен, в таком случае, из контроллера ваших маршрутов 
           (Router в FastAPI или View в Django) можно напрямую работать с функциями хранилища данных (repository_service).
"""


class EmployeeService:
    def get_all_employees(self) -> EmployeeSerializer:
        result = Employee.objects.all()
        return EmployeeSerializer(result, many=True)


    def get_employee_by_id(self, id: int) -> EmployeeSerializer:
        result = Employee.objects.filter(id=id).first()
        return EmployeeSerializer(result)


    def add_employee(self, employee: EmployeeSerializer) -> None:
        employee_data = employee.data  # получаем валидированные с помощью сериализатора данные (метод .data  возвращает объект типа dict)
        new_employee = Employee.objects.create(
            name=employee_data.get('name'),
            surname=employee_data.get('surname'),
            is_on_assingment=employee_data.get('is_on_assingment'),
        )
        new_employee.save()


    def delete_employee_by_id(self, id: str) -> None:
        Employee.objects.filter(id=id).first().delete()