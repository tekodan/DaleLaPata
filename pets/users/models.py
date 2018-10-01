from django.db import models
from django.contrib.auth.models import AbstractUser
from users.validators import validate_facebook_url
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

class Fundacion(models.Model):
    RUT = 'RUT'
    NIT = 'NIT'
    TIPO_ID = (
        (RUT, _('RUT')),
        (NIT, _('NIT')),
    )
    tipo_identificacion = models.CharField(max_length=3,
                                           choices=TIPO_ID)
    num_identificacion = models.CharField(unique=True,max_length=15)
    nombre_corto = models.CharField(max_length=100)
    razon_social = models.TextField(max_length=1000)
    descripcion = models.TextField(blank=True, null=True)
    fecha_fundacion = models.DateTimeField(blank=True, null=True)
    email = models.EmailField(unique=True, max_length=250)
    telefono = models.CharField(max_length=250, blank=True, null=True)
    logo = models.ImageField(upload_to='fundacion_profiles',
                                        help_text=_('Maximo tamaño de imagen 8mb'), blank=True, null=True)
    facebook = models.URLField(max_length=250, blank=True, null=True,
                               validators=[])
    twitter = models.URLField(max_length=250, blank=True, null=True,
                               validators=[])
    contratos = models.ForeignKey('adopcion.Contratos', models.DO_NOTHING, default=1)

    def __str__(self):
        return self.nombre_corto

class OwnerProfile(AbstractUser):
    CC = 'CC'
    TI = 'TI'
    TIPO_ID = (
        (CC, _('Cedula ciudadania')),
        (TI, _('Tarjeta identidad')),
    )
    R_01 = '1'
    R_02 = '2'
    R_03 = '3'
    TIPO_ROL = (
        (R_01, _('Responsable')),
        (R_02, _('Vinculado')),
        (R_03, _('Brigadista')),
    )
    rol = models.CharField(max_length=4, choices=TIPO_ROL, blank=True)
    tipo_identificacion = models.CharField(max_length=2,
                            choices=TIPO_ID,
                            blank=True)
    num_identificacion = models.CharField('Numero de identificación',unique=True, max_length=10)
    is_information_confirmed = models.BooleanField(default=False)
    facebook = models.URLField(max_length=250, blank=True, null=True,
                               validators=[validate_facebook_url])
    phone = models.CharField('Telefono de contacto',  max_length=30, blank=True)
    fundacion = models.ForeignKey(Fundacion, models.DO_NOTHING, db_column='fundacion', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('users:user_profile', args=[self.id])

    def get_rol(self):
        return dict(self.TIPO_ROL).get(self.rol)

    def is_responsable(self):
        if dict(self.TIPO_ROL).get(self.rol)=='Responsable' :
            return True
        return False

    def nombre_completo(self):
        return str(self.first_name)+str(' ')+str(self.last_name)

    def __str__(self):
        return self.username
