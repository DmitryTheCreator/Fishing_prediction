from django.shortcuts import render
from django.shortcuts import render, redirect
from rest_framework.generics import CreateAPIView, RetrieveDestroyAPIView, GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework import status

from .serializers import FishSerializer, WeatherSerializer, ResultSerializer, EmployeeSerializer, OrderSerializer, \
    ReportSerializer, PredictingSerializer
from .services.fish_service import FishService
from .services.employee_service import EmployeeService
from .services.order_service import OrderService
from .services.weather_service import WeatherService
from .services.report_service import ReportService
from .services.result_service import ResultService
from .services.predicting_service import PredictingService

"""
    Данный модуль отвечает за обработку соответствующих HTTP операций.

    В рамках DRF возможны следующие реализации Django Views 
    (https://www.django-rest-framework.org/tutorial/2-requests-and-responses/):

    1. View на основе функций (function based views). Такие функции должны использовать декоратор @api_view.
    2. View на основе классов (class based views). Такие классы должны наследоваться от базовых классов типа APIView 
    (подробнее о class based views см.: https://www.django-rest-framework.org/api-guide/generic-views/).

"""

fish_service = FishService()  # подключаем слой с бизнес-логикой
employee_service = EmployeeService()
order_service = OrderService()
weather_service = WeatherService()
report_service = ReportService()
result_service = ResultService()
predicting_service = PredictingService()


class GetPostPutDelFish(GenericAPIView):
    serializer_class = FishSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request: Request, *args, **kwargs) -> Response:
        """ Получить запись о виде рыбы (необходим параметр ?name=) """
        name = request.query_params.get('name')
        if name is None:
            return Response('Expecting query parameter ?name= ', status=status.HTTP_400_BAD_REQUEST)
        response = fish_service.get_fish_by_name(str(name))
        if response is not None:
            return Response(data=response.data)
        return Response(status=status.HTTP_204_NO_CONTENT)


    def post(self, request: Request, *args, **kwargs) -> Response:
        """ Добавить новую запись о виде рыбы """
        serializer = FishSerializer(data=request.data)
        if serializer.is_valid():
            fish_service.add_fish(serializer)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request: Request, *args, **kwargs) -> Response:
        """ Обновить запись о виде рыбы """
        serializer = FishSerializer(data=request.data)
        if serializer.is_valid():
            fish_service.update_fish_info(serializer)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request: Request, fish_name: str) -> Response:
        """ Удалить запись о виде рыбы """
        fish_service.delete_fish_by_name(fish_name)
        return Response(status=status.HTTP_200_OK)


class GetPostDelEmployee(GenericAPIView):
    serializer_class = EmployeeSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request: Request, *args, **kwargs) -> Response:
        """ Получить запись о сотруднике (необходим параметр ?id=) """
        id = request.query_params.get('id')
        if id is None:
            return Response('Expecting query parameter ?id= ', status=status.HTTP_400_BAD_REQUEST)
        response = employee_service.get_employee_by_id(int(id))
        if response is not None:
            return Response(data=response.data)
        return Response(status=status.HTTP_204_NO_CONTENT)


    def post(self, request: Request, *args, **kwargs) -> Response:
        """ Добавить новую запись о сотруднике """
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            employee_service.add_employee(serializer)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request: Request, id: int) -> Response:
        """ Удалить запись о сотруднике """
        employee_service.delete_fish_by_name(id)
        return Response(status=status.HTTP_200_OK)


class GetPostDelOrder(GenericAPIView):
    serializer_class = OrderSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request: Request, *args, **kwargs) -> Response:
        """ Получить запись о заказе (необходим параметр ?id=) """
        id = request.query_params.get('id')
        if id is None:
            return Response('Expecting query parameter ?id= ', status=status.HTTP_400_BAD_REQUEST)
        response = order_service.get_order_by_id(int(id))
        if response is not None:
            return Response(data=response.data)
        return Response(status=status.HTTP_204_NO_CONTENT)


    def post(self, request: Request, *args, **kwargs) -> Response:
        """ Добавить новую запись о заказе """
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order_service.create_order(serializer)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request: Request, id: int) -> Response:
        """ Удалить запись о заказе """
        order_service.delete_order_by_id(id)
        return Response(status=status.HTTP_200_OK)


class GetPostWeather(GenericAPIView):
    serializer_class = WeatherSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request: Request, *args, **kwargs) -> Response:
        """ Получить запись о погоде (необходим параметр ?id=) """
        id = request.query_params.get('id')
        if id is None:
            return Response('Expecting query parameter ?id= ', status=status.HTTP_400_BAD_REQUEST)
        response = weather_service.get_weather_entry_by_id(int(id))
        if response is not None:
            return Response(data=response.data)
        return Response(status=status.HTTP_204_NO_CONTENT)


    def post(self, request: Request, *args, **kwargs) -> Response:
        """ Добавить новую запись о погоде """
        serializer = WeatherSerializer(data=request.data)
        if serializer.is_valid():
            weather_service.create_order(serializer)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetDelAllWeather(GenericAPIView):
    serializer_class = WeatherSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request: Request, date: str) -> Response:
        """ Получить все записи о погоде за определнную дату """
        response = weather_service.get_all_weather_entry_by_date(date)
        return Response(data=response.data)


    def delete(self, request: Request, date: str) -> Response:
        """ Удалить все записи о погоде за определнную дату """
        weather_service.delete_all_weather_entry_by_date(date)
        return Response(status=status.HTTP_200_OK)


class GetPostPutDelReport(GenericAPIView):
    serializer_class = ReportSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request: Request, *args, **kwargs) -> Response:
        """ Получить запись об отчете (необходим параметр ?id=) """
        id = request.query_params.get('id')
        if id is None:
            return Response('Expecting query parameter ?id= ', status=status.HTTP_400_BAD_REQUEST)
        response = report_service.get_report_by_id(int(id))
        if response is not None:
            return Response(data=response.data)
        return Response(status=status.HTTP_204_NO_CONTENT)


    def post(self, request: Request, *args, **kwargs) -> Response:
        """ Добавить новую запись об отчете """
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            report_service.create_report(serializer)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request: Request, *args, **kwargs) -> Response:
        """ Обновить запись об отчете """
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            report_service.update_report(serializer)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request: Request, id: int) -> Response:
        """ Удалить запись об отчете """
        report_service.delete_report(id)
        return Response(status=status.HTTP_200_OK)


class GetPostPutDelResult(GenericAPIView):
    serializer_class = ResultSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request: Request, *args, **kwargs) -> Response:
        """ Получить запись о результате лова (необходим параметр ?id=) """
        id = request.query_params.get('id')  # получаем параметр id из адреса запроса, например: /api/weatherforecast?city_id=1
        if id is None:
            return Response('Expecting query parameter ?id= ', status=status.HTTP_400_BAD_REQUEST)
        response = result_service.get_result_by_id(int(id))
        if response is not None:
            return Response(data=response.data)
        return Response(status=status.HTTP_204_NO_CONTENT)


    def post(self, request: Request, *args, **kwargs) -> Response:
        """ Добавить запись о результате лова """
        serializer = ResultSerializer(data=request.data)
        if serializer.is_valid():
            result_service.add_result(serializer)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request: Request, *args, **kwargs) -> Response:
        """ Обновить запись о результате лова """
        serializer = ResultSerializer(data=request.data)
        if serializer.is_valid():
            result_service.update_result(serializer)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request: Request, id: int) -> Response:
        """ Удалить запись о результате лова """
        result_service.delete_result_by_id(id)
        return Response(status=status.HTTP_200_OK)


class GetPostPutDelPredicting(GenericAPIView):
    serializer_class = PredictingSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request: Request, *args, **kwargs) -> Response:
        """ Получить запись о предсказании лова (необходим параметр ?id=) """
        id = request.query_params.get(
            'id')  # получаем параметр id из адреса запроса, например: /api/weatherforecast?city_id=1
        if id is None:
            return Response('Expecting query parameter ?id= ', status=status.HTTP_400_BAD_REQUEST)
        response = predicting_service.get_predicting_by_id(int(id))
        if response is not None:
            return Response(data=response.data)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request: Request, *args, **kwargs) -> Response:
        """ Добавить запись о предсказании лова """
        serializer = ResultSerializer(data=request.data)
        if serializer.is_valid():
            predicting_service.add_predicting(serializer)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request: Request, *args, **kwargs) -> Response:
        """ Обновить запись о предсказании лова """
        serializer = ResultSerializer(data=request.data)
        if serializer.is_valid():
            predicting_service.update_predicting(serializer)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, id: int) -> Response:
        """ Удалить запись о предсказании лова """
        predicting_service.get_predicting_by_id(id)
        return Response(status=status.HTTP_200_OK)
