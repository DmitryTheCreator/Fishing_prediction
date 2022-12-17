import json
from random import randint, choice
from locust import HttpUser, task, tag, between
import datetime


class RESTServerUser(HttpUser):
    """ Класс, эмулирующий пользователя / клиента сервера """
    wait_time = between(1.0, 5.0)       # время ожидания пользователя перед выполнением новой task

    @tag("get_all_employees")
    @task()
    def get_all_employees(self):
        """ Тест GET-запроса (получение нескольких записей о сотрудниках) """
        self.client.get('/fishzone/employee/all')


    @tag("get_employee_id")
    @task()
    def get_employee_id(self):
        """ Тест GET-запроса (получение записи о сотруднике) """
        self.client.get(f'/fishzone/employee/{randint(1,12)}', name = '/fishzone/employee/{ID}')


    @tag("get_fish")
    @task()
    def get_fish(self):
        """ Тест GET-запроса (получение нескольких записей о видах рыб) """
        self.client.get('/fishzone/fish/all')


    @tag("get_fish_id")
    @task()
    def get_fish_id(self):
        """ Тест GET-запроса (получение записи о виде рыбы) """
        self.client.get(f'/fishzone/fish/{randint(2, 8)}', name='/fishzone/fish/{ID}')


    @tag("put_fish")
    @task()
    def put_fish(self):
        """ Тест GET-запроса (получение записи о виде рыбы) """
        self.client.put(f'/fishzone/fish/{randint(2, 8)}', json={
            "name": "рыба " + str(randint(1, 100)),
            "temperature": randint(-20, 20),
            "cloud_cover": randint(0, 5),
            "precipitation": randint(0, 4),
            "wind_speed": randint(0, 10),
            "atmospheric_pressure": randint(700, 800),
            "humidity": randint(0, 100)
        })


    @tag("get_order")
    @task()
    def get_order(self):
        """ Тест GET-запроса (получение нескольких записей о видах рыб) """
        self.client.get('/fishzone/order/all')


    @tag("get_order_id")
    @task()
    def get_order_id(self):
        """ Тест GET-запроса (получение записи о виде рыбы) """
        self.client.get(f'/fishzone/order/{randint(2, 3)}', name='/fishzone/order/{ID}')


    @tag("get_predicting")
    @task()
    def get_predicting(self):
        """ Тест GET-запроса (получение нескольких записей о видах рыб) """
        self.client.get('/fishzone/predicting/all')


    @tag("get_predicting_id")
    @task()
    def get_predicting_id(self):
        """ Тест GET-запроса (получение записи о виде рыбы) """
        self.client.get(f'/fishzone/predicting/{choice([2, 4])}', name='/fishzone/predicting/{ID}')


    @tag("put_predicting")
    @task()
    def put_predicting(self):
        """ Тест GET-запроса (получение записи о виде рыбы) """
        self.client.put(f'/fishzone/predicting/{choice([2, 4])}', json={
            "kind_of_fish_id": randint(2, 8),
            "weather_condition_id": choice([1, 2, 3, 4, 5, 7, 8])
        })


    @tag("get_report")
    @task()
    def get_report(self):
        """ Тест GET-запроса (получение нескольких записей о видах рыб) """
        self.client.get('/fishzone/report/all')


    @tag("get_report_id")
    @task()
    def get_report_id(self):
        """ Тест GET-запроса (получение записи о виде рыбы) """
        self.client.get(f'/fishzone/report/{choice([4, 6])}', name='/fishzone/report/{ID}')


    @tag("put_report")
    @task()
    def put_report(self):
        """ Тест GET-запроса (получение записи о виде рыбы) """
        self.client.put(f'/fishzone/report/{choice([4, 6])}', json={
            "order_id": randint(2, 3),
            "result_id": randint(2, 6),
            "lead_time": str(datetime.datetime.now())[:16]
        })


    @tag("get_result")
    @task()
    def get_result(self):
        """ Тест GET-запроса (получение нескольких записей о видах рыб) """
        self.client.get('/fishzone/result/all')


    @tag("get_result_id")
    @task()
    def get_result_id(self):
        """ Тест GET-запроса (получение записи о виде рыбы) """
        self.client.get(f'/fishzone/result/{randint(2, 6)}', name='/fishzone/result/{ID}')


    @tag("put_result")
    @task()
    def put_result(self):
        """ Тест GET-запроса (получение записи о виде рыбы) """
        self.client.put(f'/fishzone/result/{randint(2, 6)}', json={
            "order_id": randint(2, 3),
            "employee_id": randint(1, 12),
            "kind_of_fish_id": randint(2, 8),
            "arrival_time": str(datetime.datetime.now())[:16],
            "departure_time": str(datetime.datetime.now() - datetime.timedelta(hours=2))[:16]
        })


    @tag("get_weather")
    @task()
    def get_weather(self):
        """ Тест GET-запроса (получение нескольких записей о видах рыб) """
        self.client.get('/fishzone/weather/all')


    @tag("get_weather_id")
    @task()
    def get_weather_id(self):
        """ Тест GET-запроса (получение записи о виде рыбы) """
        self.client.get(f'/fishzone/weather/{randint(2, 6)}', name='/fishzone/weather/{ID}')


    @tag("get_weather_date")
    @task()
    def get_weather_date(self):
        """ Тест GET-запроса (получение записи о виде рыбы) """
        self.client.get(
            f'/fishzone/weather/{choice(["2022-12-07", "2022-12-08", "2022-12-09"])}',
            name='/fishzone/weather/{DATE}'
        )


    @tag("post_order")
    @task
    def post_order(self):
        json_data = {
            "customer_name": "Заказчик №" + str(randint(1, 100)),
            "deadline": str(datetime.datetime.now())[:16],
            "receiving_time": str(datetime.datetime.now() - datetime.timedelta(hours=2))[:16],
            "kind_of_fish_id": randint(2, 8),
            "fish_amount": randint(1, 100),
            "in_progress": randint(0, 1)
        }
        self.client.post(f'/fishzone/order', json_data)
