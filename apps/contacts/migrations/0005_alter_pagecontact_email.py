# Generated by Django 5.0 on 2023-12-27 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_rename_tema_pagecontact_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagecontact',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Дата'),
        ),
    ]
