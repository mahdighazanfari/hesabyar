# Generated by Django 2.2.4 on 2019-12-24 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hesabyar', '0002_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.FloatField(),
        ),
    ]
