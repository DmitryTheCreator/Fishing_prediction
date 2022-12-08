# Generated by Django 4.1.3 on 2022-12-07 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishapp', '0002_weathercondition_rename_kind_of_fish_kindoffish_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weathercondition',
            name='datetime',
        ),
        migrations.AddField(
            model_name='weathercondition',
            name='date',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='weathercondition',
            name='time',
            field=models.CharField(max_length=8, null=True),
        ),
    ]