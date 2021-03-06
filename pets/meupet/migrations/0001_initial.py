# Generated by Django 2.0.3 on 2018-10-05 17:05

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import meupet.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.TextField(max_length=100, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, max_length=30, populate_from='kind')),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('chip_id', models.IntegerField(blank=True, null=True, unique=True)),
                ('edad', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('size', models.CharField(blank=True, choices=[('SM', 'Pequeño'), ('MD', 'Mediano'), ('LG', 'Grande')], max_length=2)),
                ('sex', models.CharField(blank=True, choices=[('FE', 'Hembra'), ('MA', 'Macho')], max_length=2)),
                ('profile_picture', models.ImageField(help_text='Maximum image size is 8MB', upload_to='pet_profiles')),
                ('published', models.BooleanField(default=False)),
                ('request_sent', models.DateTimeField(blank=True, null=True)),
                ('request_key', models.CharField(blank=True, max_length=40)),
                ('active', models.BooleanField(default=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=meupet.models.get_slug, unique=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cities.City')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='PetStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=32, unique=True)),
                ('description', models.CharField(max_length=64)),
                ('final', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('description',),
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pet_photos')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='meupet.Pet')),
            ],
        ),
        migrations.CreateModel(
            name='StatusGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, max_length=64, populate_from='name', unique=True)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='petstatus',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='statuses', to='meupet.StatusGroup'),
        ),
        migrations.AddField(
            model_name='petstatus',
            name='next_status',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='meupet.PetStatus'),
        ),
    ]
