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
    path('fish/all', views.GetFish.as_view()),
    path('fish', views.PostFish.as_view()),
    path('fish/<int:id>', views.GetPutDelFishId.as_view()),
    path('employee/all', views.GetEmployee.as_view()),
    path('employee', views.PostEmployee.as_view()),
    path('employee/<int:id>', views.GetPutDelEmployeeId.as_view()),
    path('order/all', views.GetOrder.as_view()),
    path('order', views.PostOrder.as_view()),
    path('order/<int:id>', views.GetPutDelOrderId.as_view()),
    path('weather/all', views.GetWeather.as_view()),
    path('weather', views.PostWeather.as_view()),
    path('weather/<int:id>', views.GetDelWeatherId.as_view()),
    path('weather/<str:date>', views.GetDelWeatherDate.as_view()),
    path('result/all', views.GetResult.as_view()),
    path('result', views.PostResult.as_view()),
    path('result/<int:id>', views.GetPutDelResultId.as_view()),
    path('report/all', views.GetReport.as_view()),
    path('report', views.PostReport.as_view()),
    path('report/<int:id>', views.GetPutDelReportId.as_view()),  
    path('predicting/all', views.GetPredicting.as_view()),
    path('predicting/<str:date>', views.GetPredictingByDate.as_view()),
    path('predicting', views.PostPredicting.as_view()),
    path('predicting/<int:id>', views.GetPutDelPredictingId.as_view()),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
