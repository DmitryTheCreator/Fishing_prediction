# Generated by Django 4.1.3 on 2022-12-07 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fishapp', '0004_result_departure_time_result_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='fish_amount',
        ),
    ]
