# Generated by Django 4.1.3 on 2022-12-21 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("fishapp", "0011_rename_predict_order_predicting"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="predicting",
        ),
    ]
