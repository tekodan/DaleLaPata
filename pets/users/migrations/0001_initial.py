# Generated by Django 2.0.3 on 2018-10-01 21:02

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import users.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='OwnerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('rol', models.CharField(blank=True, choices=[('1', 'Responsable'), ('2', 'Vinculado'), ('3', 'Brigadista')], max_length=4)),
                ('tipo_identificacion', models.CharField(blank=True, choices=[('CC', 'Cedula ciudadania'), ('TI', 'Tarjeta identidad')], max_length=2)),
                ('num_identificacion', models.CharField(max_length=10, unique=True, verbose_name='Numero de identificación')),
                ('is_information_confirmed', models.BooleanField(default=False)),
                ('facebook', models.URLField(blank=True, max_length=250, null=True, validators=[users.validators.validate_facebook_url])),
                ('phone', models.CharField(blank=True, max_length=30, verbose_name='Telefono de contacto')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Fundacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_identificacion', models.CharField(choices=[('RUT', 'RUT'), ('NIT', 'NIT')], max_length=3)),
                ('num_identificacion', models.CharField(max_length=15, unique=True)),
                ('nombre_corto', models.CharField(max_length=100)),
                ('razon_social', models.TextField(max_length=1000)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('fecha_fundacion', models.DateTimeField(blank=True, null=True)),
                ('email', models.EmailField(max_length=250, unique=True)),
                ('telefono', models.CharField(blank=True, max_length=250, null=True)),
                ('logo', models.ImageField(blank=True, help_text='Maximo tamaño de imagen 8mb', null=True, upload_to='fundacion_profiles')),
                ('facebook', models.URLField(blank=True, max_length=250, null=True)),
                ('twitter', models.URLField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='ownerprofile',
            name='fundacion',
            field=models.ForeignKey(blank=True, db_column='fundacion', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.Fundacion'),
        ),
        migrations.AddField(
            model_name='ownerprofile',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='ownerprofile',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
