# Generated by Django 3.1 on 2021-10-19 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equeue', '0006_auto_20211007_1638'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QueuedCustomer',
        ),
    ]
