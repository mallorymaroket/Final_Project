# Generated by Django 3.1.7 on 2021-04-11 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questboard', '0006_createquestboard_hi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createquestboard',
            name='hi',
        ),
    ]