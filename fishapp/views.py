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


class GetFish(GenericAPIView):
    serializer_class = FishSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request: Request, *args, **kwargs) -> Response:
        """ Получить все записи о видах рыб """
        response = fish_service.get_all_fish()
        return Response(data=response.data)


class PostFish(GenericAPIView):
    serializer_class = FishSerializer
    renderer_classes = [JSONRenderer]

    def post(self, request: Request, *args, **kwargs) -> Response:
        """ Добавить новую запись о виде рыбы """
        serializer = FishSerializer(data=request.data)
        if serializer.is_valid():
            fish_service.add_fish(serializer)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetPutDelFishId(GenericAPIView):
    serializer_class = FishSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request: Request, id: int) -> Response:
        """ Получить запись о виде рыбы """
        response = fish_service.get_fish_by_id(id)
        if response is not None:
            return Response(data=response.data)
        return Response(status=status.HTTP_204_NO_CONTENT)


    def put(self, request: Request, *args, id: int) -> Response:
        """ Обновить запись о виде рыбы """
        serializer = FishSerializer(data=request.data)
        if serializer.is_valid():
            fish_service.update_fish_info_by_id(fish=serializer, id=id)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request: Request, id: int) -> Response:
        """ Удалить запись о виде рыбы """
        fish_service.delete_fish_by_id(id)
        return Response(status=status.HTTP_200_OK)


class GetEmployee(GenericAPIView):
    serializer_class = EmployeeSerializer
    renderer_classes = [JSONRenderer]


    def get(self, request: Request, *args, **kwargs) -> Response:
        """ Получить все записи о сотрудниках """
        response = employee_service.get_all_employees()
        return Response(data=response.data)


class PostEmployee(GenericAPIView):
    serializer_class = EmployeeSerializer
    renderer_classes = [JSONRenderer]

    def post(self, request: Request, *args, **kwargs) -> Response:
        """ Добавить новую запись о виде рыбы """
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            employee_service.add_employee(serializer)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetPutDelEmployeeId(GenericAPIView):
    serializer_class = EmployeeSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request: Request, id: int) -> Response:
        """ Получить запись о сотруднике """
        response = employee_service.get_employee_by_id(id)
        if response is not None:
            return Response(data=response.data)
        return Response(status=status.HTTP_204_NO_CONTENT)


    def put(self, request: Request, *args, id: int) -> Response:
        """ Обновить запись о сотруднике """
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            employee_service.update_employee(serializer, id=id)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request: Request, id: int) -> Response:
        """ Удалить запись о сотруднике """
        employee_service.delete_employee_by_id(id)
        return Response(status=status.HTTP_200_OK)


class GetOrder(GenericAPIView):
    serializer_class = OrderSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request: Request, *args, **kwargs) -> Response:
        """ Получить все записи о заказах """
        response = order_service.get_all_orders()
        return Response(data=response.data)


class PostOrder(GenericAPIView):
    serializer_class = OrderSerializer
    renderer_classes = [JSONRenderer]

    def post(self, request: Request, *args, **kwargs) -> Response:
        """ Добавить новую запись о заказе """
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order_service.create_order(serializer)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetPutDelOrderId(GenericAPIView):
    serializer_class = OrderSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request: Request, id: int) -> Response:
        """ Получить запись о заказе """
        response = order_service.get_order_by_id(id)
        if response is not None:
            return Response(data=response.data)
        return Response(status=status.HTTP_204_NO_CONTENT)


    def put(self, request: Request, *args, id: int) -> Response:
        """ Обновить запись о заказе """
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order_service.update_order(serializer, id=id)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request: Request, id: int) -> Response:
        """ Удалить запись о заказе """
        order_service.delete_order_by_id(id)
        return Response(status=status.HTTP_200_OK)


class GetWeather(GenericAPIView):
    serializer_class = WeatherSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request: Request, *args, **kwargs) -> Response:
        """ Получить все записи о погодных условиях """
        response = weather_service.get_all_weather_entries()
        return Response(data=response.data)


class PostWeather(GenericAPIView):
    serializer_class = WeatherSerializer
    renderer_classes = [JSONRenderer]

    def post(self, request: Request, *args, **kwargs) -> Response:
        """ Добавить новую запись о погоде """
        serializer = WeatherSerializer(data=request.data)
        if serializer.is_valid():
            weather_service.add_weather_entry(serializer)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class GetDelWeatherId(GenericAPIView):
    serializer_class = WeatherSerializer
    renderer_classes = [JSONRenderer]


    def get(self, request: Request, id: int) -> Response:
        """ Получить запись о погоде """
        response = weather_service.get_weather_entry_by_id(id)
        if response is not None:
            return Response(data=response.data)
        return Response(status=status.HTTP_204_NO_CONTENT)


    def delete(self, request: Request, id: int) -> Response:
        """ Удалить запись о погоде """
        weather_service.delete_weather_entry_by_id(id)
        return Response(status=status.HTTP_200_OK)


class GetDelWeatherDate(GenericAPIView):
    serializer_class = WeatherSerializer
    renderer_classes = [JSONRenderer]


    def get(self, request: Request, date: str) -> Response:
        """ Получить все записи о погоде по дате """
        response = weather_service.get_all_weather_entries_by_date(date)
        if response is not None:
            return Response(data=response.data)
        return Response(status=status.HTTP_204_NO_CONTENT)


    def delete(self, request: Request, date: str) -> Response:
        """ Удалить все записи о погоде по дате """
        weather_service.delete_all_weather_entries_by_date(date)
        return Response(status=status.HTTP_200_OK)


class GetResult(GenericAPIView):
    serializer_class = ResultSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request: Request, *args, **kwargs) -> Response:
        """ Получить все записи о результатах лова """
        response = result_service.get_all_results()
        return Response(data=response.data)


class PostResult(GenericAPIView):
    serializer_class = ResultSerializer
    renderer_classes = [JSONRenderer]

    def post(self, request: Request, *args, **kwargs) -> Response:
        """ Добавить новую запись о результате лова """
        serializer = ResultSerializer(data=request.data)
        if serializer.is_valid():
            result_service.add_result(serializer)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class GetPutDelResultId(GenericAPIView):
    serializer_class = ResultSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request: Request, id: int) -> Response:
        """ Получить запись о результате лова """
        response = result_service.get_result_by_id(id)
        if response is not None:
            return Response(data=response.data)
        return Response(status=status.HTTP_204_NO_CONTENT)


    def put(self, request: Request, *args, id: int) -> Response:
        """ Обновить запись о результате лова """
        serializer = ResultSerializer(data=request.data)
        if serializer.is_valid():
            result_service.update_result(result=serializer, id=id)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request: Request, id: int) -> Response:
        """ Удалить запись о результате лова """
        result_service.delete_result_by_id(id)
        return Response(status=status.HTTP_200_OK)
    
    
class GetReport(GenericAPIView):
    serializer_class = ReportSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request: Request, *args, **kwargs) -> Response:
        """ Получить все записи об отчетах """
        response = report_service.get_all_reports()
        return Response(data=response.data)


class PostReport(GenericAPIView):
    serializer_class = ReportSerializer
    renderer_classes = [JSONRenderer]

    def post(self, request: Request, *args, **kwargs) -> Response:
        """ Добавить новую запись об отчете """
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            report_service.create_report(serializer)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetPutDelReportId(GenericAPIView):
    serializer_class = ReportSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request: Request, id: int) -> Response:
        """ Получить запись об отчете """
        response = report_service.get_report_by_id(id)
        if response is not None:
            return Response(data=response.data)
        return Response(status=status.HTTP_204_NO_CONTENT)


    def put(self, request: Request, *args, id: int) -> Response:
        """ Обновить запись об отчете """
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            report_service.update_report(report=serializer, id=id)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request: Request, id: int) -> Response:
        """ Удалить запись об отчете """
        report_service.delete_report(id)
        return Response(status=status.HTTP_200_OK)


class GetPredicting(GenericAPIView):
    serializer_class = PredictingSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request: Request, *args, **kwargs) -> Response:
        """ Получить все записи о предсказании лова """
        response = predicting_service.get_all_predicitngs()
        return Response(data=response.data)


class GetPredictingByDate(GenericAPIView):
    serializer_class = PredictingSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request: Request, date: str) -> Response:
        """ Получить все записи за 3 дня о предсказании лова """
        response = predicting_service.get_all_predicitngs_by_date(date)
        return Response(data=response.data)


class PostPredicting(GenericAPIView):
    serializer_class = PredictingSerializer
    renderer_classes = [JSONRenderer]

    def post(self, request: Request, *args, **kwargs) -> Response:
        """ Добавить новую запись о предсказании лова """
        serializer = PredictingSerializer(data=request.data)
        if serializer.is_valid():
            predicting_service.add_predicting(serializer)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class GetPutDelPredictingId(GenericAPIView):
    serializer_class = PredictingSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request: Request, id: int) -> Response:
        """ Получить запись о предсказании лова """
        response = predicting_service.get_predicting_by_id(id)
        if response is not None:
            return Response(data=response.data)
        return Response(status=status.HTTP_204_NO_CONTENT)


    def put(self, request: Request, id: int) -> Response:
        """ Обновить запись о предсказании лова """
        serializer = PredictingSerializer(data=request.data)
        if serializer.is_valid():
            predicting_service.update_predicting(predicting=serializer, id=id)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request: Request, id: int) -> Response:
        """ Удалить запись о предсказании лова """
        predicting_service.delete_predicting_by_id(id)
        return Response(status=status.HTTP_200_OK)
