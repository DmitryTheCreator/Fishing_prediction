from django.contrib import admin
from .models import *

"""
    В данном модуле регистрируются модели Django 
    для доступа через веб-интерфейс админиcтратора (django-admin)
"""

admin.site.register(Report)
admin.site.register(KindOfFish)
admin.site.register(WeatherCondition)
admin.site.register(Predicting)
admin.site.register(Order)
admin.site.register(Result)
admin.site.register(Employee)
