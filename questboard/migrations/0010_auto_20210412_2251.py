# Generated by Django 3.1.7 on 2021-04-12 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questboard', '0009_auto_20210412_2245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='createquest',
            old_name='createquestboard',
            new_name='questboard',
        ),
    ]