# Generated by Django 4.1.3 on 2022-12-17 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fishapp", "0009_rename_predicting_order_predict"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="performance",
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="kindoffish",
            name="fishing_time",
            field=models.FloatField(null=True),
        ),
    ]
