# Generated by Django 5.0 on 2023-12-27 10:10

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0014_blogdetail'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogDetail',
        ),
        migrations.AddField(
            model_name='news',
            name='descriptions1',
            field=ckeditor.fields.RichTextField(default=1, verbose_name='Описание1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='letter',
            field=models.TextField(default=1, verbose_name='Письмо текст'),
            preserve_default=False,
        ),
    ]