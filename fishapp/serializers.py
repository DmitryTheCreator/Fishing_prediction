from rest_framework import serializers

"""
    В данном модуле реализуются сериализаторы DRF, позволяющие 
    валидировать данные для моделей DAO (models.py), 
    а также сериализующие (преобразующие) эти модели в стандартные 
    объекты Python (dict) и в формат json. Подробнее см.: 
    https://www.django-rest-framework.org/api-guide/serializers/
    https://www.django-rest-framework.org/api-guide/fields/

    Сериализаторы DRF являются аналогом DTO для Django. 
"""


class FishSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    temperature = serializers.IntegerField(required=False)
    cloud_cover = serializers.IntegerField(required=False)
    precipitation = serializers.IntegerField(required=False)
    wind_speed = serializers.IntegerField(required=False)
    atmospheric_pressure = serializers.IntegerField(required=False)
    humidity = serializers.IntegerField(required=False)
    fishing_time = serializers.FloatField(required=False)

    """ Класс Serializer позволяет переопределить наследуемые 
        методы create() и update(), в которых, например, можно реализовать бизнес-логику 
        для сохранения или обновления валидируемого объекта (например, для DAO ) """


class WeatherSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    temperature = serializers.IntegerField(required=False)
    cloud_cover = serializers.IntegerField(required=False)
    precipitation = serializers.IntegerField(required=False)
    wind_speed = serializers.IntegerField(required=False)
    atmospheric_pressure = serializers.IntegerField(required=False)
    humidity = serializers.IntegerField(required=False)
    date = serializers.CharField(required=False)
    time = serializers.CharField(required=False)


class PredictingSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    order_id = serializers.IntegerField()
    weather_condition_id = serializers.IntegerField()
    predict = serializers.IntegerField()
    date = serializers.CharField(required=False)


class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    customer_name = serializers.CharField(required=False)
    deadline = serializers.CharField(required=False)
    receiving_time = serializers.CharField(required=False)
    kind_of_fish_id = serializers.IntegerField()
    fish_amount = serializers.FloatField(required=False)
    in_progress = serializers.IntegerField(required=False)


class ResultSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    order_id = serializers.IntegerField()
    employee_id = serializers.IntegerField()
    kind_of_fish_id = serializers.IntegerField()
    arrival_time = serializers.CharField(required=False)
    departure_time = serializers.CharField(required=False)


class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(required=False)
    surname = serializers.CharField(required=False)
    is_on_assingment = serializers.IntegerField(required=False)
    performance = serializers.IntegerField(required=False)


class ReportSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    order_id = serializers.IntegerField()
    result_id = serializers.IntegerField()
    lead_time = serializers.CharField(required=False)
    updated_on = serializers.DateTimeField(required=False)
    created_on = serializers.DateTimeField(required=False)
