# Generated by Django 2.0.3 on 2018-09-14 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyFundacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_identificacion', models.CharField(blank=True, choices=[('RUT', 'RUT'), ('NIT', 'NIT')], max_length=3)),
                ('num_identificacion', models.CharField(max_length=15, unique=True)),
                ('razon_social', models.CharField(blank=True, max_length=250, null=True)),
                ('fecha_fundacion', models.DateTimeField(blank=True, null=True)),
                ('email', models.CharField(max_length=250, unique=True)),
                ('telefono', models.CharField(blank=True, max_length=250, null=True)),
                ('logo', models.ImageField(help_text='Maximo tamaño de imagen 8mb', upload_to='fundacion_profiles')),
                ('facebook', models.URLField(blank=True, max_length=250, null=True)),
                ('twitter', models.URLField(blank=True, max_length=250, null=True)),
                ('contrato_base', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'my_fundacion',
                'managed': False,
            },
        ),
        migrations.AddField(
            model_name='ownerprofile',
            name='fundacion',
            field=models.ForeignKey(blank=True, db_column='fundacion', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.MyFundacion'),
        ),
    ]
