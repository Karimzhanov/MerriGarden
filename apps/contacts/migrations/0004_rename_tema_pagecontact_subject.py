# Generated by Django 5.0 on 2023-12-27 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_pagecontact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pagecontact',
            old_name='tema',
            new_name='subject',
        ),
    ]