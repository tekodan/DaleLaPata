# Generated by Django 2.0.3 on 2018-10-01 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fundacion',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fundacion',
            name='nombre_corto',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fundacion',
            name='razon_social',
            field=models.TextField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
