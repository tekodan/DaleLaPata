# Generated by Django 2.0.3 on 2018-09-24 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0004_auto_20180924_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clausulas_base',
            name='descripcion',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='clausulas_fundacion',
            name='descripcion',
            field=models.TextField(max_length=2000),
        ),
    ]
