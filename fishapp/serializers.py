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
    name = serializers.CharField()
    temperature = serializers.IntegerField(required=False)
    cloud_cover = serializers.IntegerField(required=False)
    precipitation = serializers.IntegerField(required=False)
    wind_speed = serializers.IntegerField(required=False)
    atmospheric_pressure = serializers.IntegerField(required=False)
    humidity = serializers.IntegerField(required=False)

    """ Класс Serializer позволяет переопределить наследуемые 
        методы create() и update(), в которых, например, можно реализовать бизнес-логику 
        для сохранения или обновления валидируемого объекта (например, для DAO ) """


class WeatherSerializer(serializers.Serializer):
    temperature = serializers.IntegerField(required=False)
    cloud_cover = serializers.IntegerField(required=False)
    precipitation = serializers.IntegerField(required=False)
    wind_speed = serializers.IntegerField(required=False)
    atmospheric_pressure = serializers.IntegerField(required=False)
    humidity = serializers.IntegerField(required=False)


class PredictingSerializer(serializers.Serializer):
    kind_of_fish = serializers.CharField()
    weather_condition = serializers.CharField()


class OrderSerializer(serializers.Serializer):
    customer_name = serializers.CharField(required=False)
    deadline = serializers.CharField(required=False)
    receiving_time = serializers.CharField(required=False)
    kind_of_fish = serializers.CharField(required=False)
    fish_amount = serializers.FloatField(required=False)
    in_progress = serializers.IntegerField(required=False)


class ResultSerializer(serializers.Serializer):
    order = serializers.CharField(required=False)
    employee = serializers.CharField(required=False)
    kind_of_fish = serializers.CharField(required=False)
    arrival_time = serializers.CharField(required=False)
    departure_time = serializers.FloatField(required=False)


class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    surname = serializers.CharField(required=False)
    is_on_assingment = serializers.IntegerField(required=False)


class ReportSerializer(serializers.Serializer):
    order = serializers.CharField(required=False)
    result = serializers.CharField(required=False)
    lead_time = serializers.CharField(required=False)
    updated_on = serializers.DateTimeField(required=False)
    created_on = serializers.DateTimeField(required=False)
