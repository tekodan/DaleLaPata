# Generated by Django 2.0.3 on 2018-09-21 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fundacion',
            name='tipo_identificacion',
            field=models.CharField(choices=[('RUT', 'RUT'), ('NIT', 'NIT')], max_length=3),
        ),
    ]
