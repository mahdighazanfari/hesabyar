# Generated by Django 2.2.4 on 2019-12-31 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hesabyar', '0003_auto_20191224_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionmember',
            name='transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hesabyar.Transaction'),
        ),
    ]
