# Generated by Django 3.2.5 on 2021-07-25 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('football_api_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='football',
            old_name='nationality',
            new_name='manager',
        ),
    ]