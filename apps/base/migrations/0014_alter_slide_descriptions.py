# Generated by Django 5.0 on 2024-04-30 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_alter_slide_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='descriptions',
            field=models.TextField(verbose_name='Описание'),
        ),
    ]
