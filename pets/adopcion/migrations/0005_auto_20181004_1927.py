# Generated by Django 2.0.3 on 2018-10-05 00:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0004_auto_20181004_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seguimiento',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 5, 0, 27, 58, 334430, tzinfo=utc)),
        ),
    ]