# Generated by Django 4.1.3 on 2022-12-14 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishapp', '0006_alter_employee_table_alter_report_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='in_progress',
            field=models.IntegerField(),
        ),
    ]