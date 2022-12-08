from django.urls import path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from . import views

"""
    Подключение URI для приложения fishapp.
    Корневые URI представлены в базовом модуле application/urls.py
"""

# Метаданные Swagger
schema_view = get_schema_view(
   openapi.Info(
      title="FishZone API",
      default_version='v1',
      description="FishZone - сервис прогнозирования расположения мест, наиболее "
                  "пригодных для ловли рыбы с точки зрения внешних факторов",
      terms_of_service="http://192.168.56.104/wp/",
      contact=openapi.Contact(email="dmitriyzamorev@gmail.com"),
      license=openapi.License(name="Shapito license"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
   
    path('fish', views.GetPostPutDelFish.as_view()),
    path('employee', views.GetPostDelEmployee.as_view()),
    path('report', views.GetPostPutDelReport.as_view()),
    path('order', views.GetPostDelOrder.as_view()),
    path('weather', views.GetPostWeather.as_view()),
    path('weather/<str:date>', views.GetDelAllWeather.as_view()),
    path('result', views.GetPostPutDelResult.as_view()),
    path('predicting', views.GetPostPutDelPredicting.as_view()),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
