# Generated by Django 5.0 on 2023-12-26 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('number', models.CharField(max_length=255, verbose_name='Номер телефона')),
                ('data', models.DateTimeField(verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Запрос на связь',
                'verbose_name_plural': 'Запросы на связь',
            },
        ),
    ]
