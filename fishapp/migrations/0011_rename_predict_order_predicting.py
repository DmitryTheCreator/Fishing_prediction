# Generated by Django 4.1.3 on 2022-12-21 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fishapp', '0010_employee_performance_kindoffish_fishing_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='predict',
            new_name='predicting',
        ),
    ]