# Generated by Django 4.1.3 on 2022-12-17 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("fishapp", "0008_order_predicting"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order",
            old_name="predicting",
            new_name="predict",
        ),
    ]
