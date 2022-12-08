from ..serializers import ReportSerializer
from .repository_service import *
from ..models import Report

"""
    Данный модуль содержит программный слой с реализацией дополнительной бизнес-логики, 
    выполняемой перед или после выполнения операций над хранилищем данных (repository), 
    а также выполнение дополнительных операций над сериализаторами (если необходимо).

    ВАЖНО! Реализация данного слоя приведена в качестве демонстрации полной структуры RESTful веб-сервиса.
           В небольших проектах данный слой может быть избыточен, в таком случае, из контроллера ваших маршрутов 
           (Router в FastAPI или View в Django) можно напрямую работать с функциями хранилища данных (repository_service).
"""


class ReportService:
    def get_report_by_id(self, id: int) -> Optional[Report]:
        result = Report.objects.filter(id=id).first()
        if result is not None:
            return ReportSerializer(result)
        return result

    def create_report(self, report: ReportSerializer) -> None:
        report_data = report.data  # получаем валидированные с помощью сериализатора данные (метод .data  возвращает объект типа dict)
        new_report = Report.objects.create(
            order=report_data.get('order'),
            result=report_data.get('result'),
            lead_time=report_data.get('lead_time'),
        )
        new_report.save()

    def update_report(self, report: ReportSerializer) -> None:
        report_data = report.data
        report_gotten = Report.objects.filter(id=report_data.get('id'))
        report_gotten.order = report_data.get('order')
        report_gotten.result = report_data.get('result')
        report_gotten.lead_time = report_data.get('lead_time')
        report_gotten.save()
        
    def delete_report(self, id: int) -> None:
        Report.objects.filter(id=id).delete()
