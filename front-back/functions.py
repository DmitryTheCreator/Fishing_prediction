from predicting.predicting import predicting
from fishapp.models import Predicting, WeatherCondition
from datetime import date, timedelta
from fishapp.services.predicting_service import PredictingService

def give_predict(order_id: int):
    first_day_predict = predicting(order_id=order_id)
    second_day_predict = predicting(order_id=order_id, url_day='tomorrow/')
    third_day_predict = predicting(order_id=order_id, url_day='3-day/')
    days_predict = [first_day_predict, second_day_predict, third_day_predict]

    first_day_weather = WeatherCondition.objects.filter(date=str(date.today())).all()
    second_day_weather = WeatherCondition.objects.filter(date=str(date.today() + timedelta(days=1))).all()
    third_day_weather = WeatherCondition.objects.filter(date=str(date.today() + timedelta(days=2))).all()
    days_weather = [first_day_weather, second_day_weather, third_day_weather]

    for day in range(len(days_weather)):
        for hour in range(len(lenfirst_day_predict)):
            new_predicting = Predicting.objects.create(
                order_id=order_id,
                weather_condition_id=days_weather[day][hour],
                predict=days_predict[day][hour]
            )
            new_predicting.save()
    predicting_service = PredictingService()
    return [
        predicting_service.get_all_predicitngs_by_day(str(date.today())),
        predicting_service.get_all_predicitngs_by_day(str(date.today() + timedelta(days=1))),
        predicting_service.get_all_predicitngs_by_day(str(date.today() + timedelta(days=2)))
        ]


