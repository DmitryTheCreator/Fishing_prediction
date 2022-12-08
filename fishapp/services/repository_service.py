from typing import Optional, Iterable, List
from django.db.models import QuerySet
# Импортируем модели DAO
from ..models import KindOfFish


"""

    Данный модуль является промежуточным слоем приложения, который отделяет операции 
    для работы с моделями DAO от основной бизнес-логики приложения. Создание данного 
    слоя позволяет унифицировать функции работы с источником данных, и, например, если 
    в приложении нужно будет использовать другой framework для работы с БД, вы можете 
    создать новый модуль (repository_service_newframework.py) и реализовать в нем функции 
    с аналогичными названиями (get_weather_by_city_id, и т.д.). Новый модуль можно будет
    просто импортировать в модуль с основной бизнес-логикой, практически не меняя при этом
    остальной код.
    Также отделение функций работы с БД можно сделать через отдельный абстрактный класс и 
    использовать порождающий паттерн для переключения между необходимыми реализацииями.

"""


def get_fish_by_name(name: str) -> Optional[KindOfFish]:
    """ Поиск рыбы по названию вида """
    fish = Kind_of_fish.objects.filter(name=name)
    return fish


def get_weather_by_city_name(city_name: str) -> QuerySet:
    """ Выборка всех записей о погоде по наименованию населённого пункта """
    weather = Weather.objects.select_related('city').filter(city__name=city_name).all()
    # объект Weather и связанные объекты City (сфильтром по city_name) будут получены
    # через JOIN-запрос, т.о. при вызове weather.city дополнительных SQL-запросов не будет
    # Конструкция city__name означает обращение к полю "name" объекта City, связанного с Weather через поле "city"
    return weather


def create_weather(temp_c: float, pressure: int, city_id: int, weather_type: int) -> None:
    """ Создание нового объекта Weather и добавление записи о погоде """
    weather = Weather.objects.create(temperature_c=temp_c, pressure=pressure, city_id=city_id, type_id=weather_type)
    weather.save()


def update_weather_temp_and_pressure(temp_c: float, pressure: int, city_id: int) -> None:
    """ Обновление значений температуры и давления (самой старой записи)
        для заданного населённого пункта """
    weather = get_weather_by_city_id(city_id)
    weather.temperature_c = temp_c
    weather.pressure = pressure
    weather.save()


def delete_weather_by_city_name(city_name: str) -> None:
    """ Удаление записей о погоде в указанном населённом пункте """
    get_weather_by_city_name(city_name).delete()


def add_city(city_name: str) -> None:
    """ Добавление нового населённого пункта """
    city = City.objects.create(name=city_name)
    city.save()


def add_weather_type(weather_type_name: str) -> None:
    """ Добавление нового типа погоды """
    weather_type = WeatherType.objects.create(type=weather_type_name)
    weather_type.save()
