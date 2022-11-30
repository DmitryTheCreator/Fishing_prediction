from django.db.models import *
from django.utils import timezone
from django.db import models
from django.conf import settings

# Create your models here.


# class Weather(Model):
#     id = AutoField(primary_key=True)     # объявление первичного ключа с автоикрементом
#     _temperature_c = DecimalField(null=False, max_digits=5, decimal_places=2)    # поле не может быть пустым (NULL)
#     temperature_f = DecimalField(null=False, max_digits=5, decimal_places=2)
#     pressure = IntegerField(null=True)
#     # связь полей type и city через внешние ключи
#     type = ForeignKey('WeatherType', null=False, on_delete=CASCADE)
#     city = ForeignKey('City', null=False, on_delete=CASCADE)
#     created_on = DateTimeField(auto_now_add=True)   # в поле автоматически генерируется метка времени при создании записи
#     updated_on = DateTimeField(auto_now=True)       # в поле автоматически генерируется метка времени при создании записи, метка обновляется при каждой операции UPDATE
#
#     class Meta:
#         """ Установка названия таблицы """
#         db_table = 'weather'
#
#     @property
#     def temperature_c(self):
#         """ Стандартные декораторы @property и @setter позволяют задать дополнительную
#             бизнес-логику или проверку при присвоении атрибуту модели какого-либо значения """
#         return self._temperature_c
#
#     @temperature_c.setter
#     def temperature_c(self, temperature_c: float):
#         """ При установке значения полю temperature_c будет автоматически рассчитано значение temperature_f """
#         self.temperature_f = 32.0 + (temperature_c / 0.5556)
#         self._temperature_c = temperature_c
#
#     def __str__(self):
#         """ Метод определяет строковое представление модели """
#         return str({'temperature_c': self.temperature_c, 'temperature_f': self.temperature_f,
#                     'type': self.type, 'city': self.city, 'created_on': self.created_on, 'updated_on': self.updated_on})

"""--------------------------------------------------------------------------------------------"""

class Report(models.Model):
    id = AutoField(primary_key=True)     # объявление первичного ключа с автоикрементом
    order = ForeignKey('Order', null=False, on_delete=CASCADE)
    result = ForeignKey('Result', null=False, on_delete=CASCADE)
    lead_time = CharField(max_length=20, null=False, unique=False)
    created_on = DateTimeField(auto_now_add=True)  # в поле автоматически генерируется метка времени при создании записи
    updated_on = DateTimeField(auto_now=True)  # в поле автоматически генерируется метка времени при создании записи, метка обновляется при каждой операции UPDATE

    class Meta:
        """ Установка названия таблицы """
        db_table = 'report'

    # @property
    # def temperature_c(self):
    #     """ Стандартные декораторы @property и @setter позволяют задать дополнительную
    #         бизнес-логику или проверку при присвоении атрибуту модели какого-либо значения """
    #     return self._temperature_c
    #
    # @temperature_c.setter
    # def temperature_c(self, temperature_c: float):
    #     """ При установке значения полю temperature_c будет автоматически рассчитано значение temperature_f """
    #     self.temperature_f = 32.0 + (temperature_c / 0.5556)
    #     self._temperature_c = temperature_c

    def __str__(self):
        """ Метод определяет строковое представление модели """
        return str({'order': self.order, 'results': self.result, 'lead_time': self.lead_time,
                    'created_on': self.created_on, 'updated_on': self.updated_on})


class Kind_of_fish(models.Model):
    """ Тип рыбы """
    id = AutoField(primary_key=True)
    name = CharField(max_length=20, null=False, unique=False)
    temperature = IntegerField(null=True)
    cloud_cover = IntegerField(null=True)
    precipitation = IntegerField(null=True)
    wind_speed = IntegerField(null=True)
    atmospheric_pressure = IntegerField(null=True)
    humidity = IntegerField(null=True)


    class Meta:
        db_table = 'kind_of_fish'

    def __str__(self):
        return str({'id': self.id, 'name': self.name, 'temperature': self.temperature,
                    'cloud_cover': self.cloud_cover, 'precipitation': self.precipitation,
                    'wind_speed': self.cloud_cover, 'atmospheric_pressure': self.atmospheric_pressure,
                    'humidity': self.humidity})



class Weather_condition(models.Model):
    """ Погодные условия """
    id = AutoField(primary_key=True)
    temperature = IntegerField(null=True)
    cloud_cover = IntegerField(null=True)
    precipitation = IntegerField(null=True)
    wind_speed = IntegerField(null=True)
    atmospheric_pressure = IntegerField(null=True)
    humidity = IntegerField(null=True)


    class Meta:
        db_table = 'weather_condition'

    def __str__(self):
        return str({'id': self.id, 'temperature': self.temperature, 'cloud_cover': self.cloud_cover,
                    'precipitation': self.precipitation, 'wind_speed': self.cloud_cover,
                    'atmospheric_pressure': self.atmospheric_pressure, 'humidity': self.humidity})




class Predicting(models.Model):
    """ Предсказание """
    id = AutoField(primary_key=True)  # объявление первичного ключа с автоикрементом
    kind_of_fish = ForeignKey('Kind_of_fish', null=False, on_delete=CASCADE)
    weather_condition = ForeignKey('Weather_condition', null=False, on_delete=CASCADE)

    class Meta:
        db_table = 'predicting'

    def __str__(self):
        return str({'id': self.id, 'kind_of_fish': self.kind_of_fish,
                    'weather_condition': self.weather_condition})


class Order(models.Model):
    """ Заказы """
    id = AutoField(primary_key=True)
    customer_name = CharField(max_length=20, null=False, unique=False)
    deadline = CharField(max_length=20, null=False, unique=False)
    receiving_time = CharField(max_length=20, null=False, unique=False)
    kind_of_fish = ForeignKey('Kind_of_fish', null=False, on_delete=CASCADE)
    fish_amount = FloatField(null=False, unique=False)
    in_progress = BooleanField(null=False, unique=False)

    class Meta:
        db_table = 'order'

    def __str__(self):
        return str({'id': self.id, 'customer_name': self.customer_name, 'deadline': self.deadline,
                    'receiving_time': self.receiving_time, 'kind_of_fish': self.kind_of_fish,
                    'fish_amount': self.fish_amount, 'in_progress': self.in_progress})


class Result(models.Model):
    """ Результаты лова """
    id = AutoField(primary_key=True)
    employee = ForeignKey('Employee', null=False, on_delete=CASCADE)
    kind_of_fish = ForeignKey('Kind_of_fish', null=False, on_delete=CASCADE)
    fish_amount = FloatField(null=False, unique=False)
    arrival_time = CharField(max_length=20, null=False, unique=False)

    class Meta:
        db_table = 'result'

    def __str__(self):
        return str({'id': self.id, 'employee': self.employee, 'kind_of_fish': self.kind_of_fish,
                    'fish_amount': self.fish_amount, 'arrival_time': self.arrival_time})



class Employee(models.Model):
    """ Работники """
    id = AutoField(primary_key=True)
    name = CharField(max_length=20, null=False, unique=False)
    surname = CharField(max_length=20, null=False, unique=False)
    is_on_assingment = BooleanField(null=False, unique=False)

    class Meta:
        db_table = 'employee'

    def __str__(self):
        return str({'id': self.id, 'name': self.name, 'surname': self.surname,
                    'is_on_assingment': self.is_on_assingment})
