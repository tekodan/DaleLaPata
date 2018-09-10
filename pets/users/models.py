from django.db import models
from django.contrib.auth.models import AbstractUser
from users.validators import validate_facebook_url
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

class OwnerProfile(AbstractUser):
    CC = 'CC'
    TI = 'TI'
    TIPO_ID = (
        (CC, _('Cedula ciudadania')),
        (TI, _('Tarjeta identidad')),
    )
    R_01 = 'R_01'
    R_02 = 'R_02'
    R_03 = 'R_03'
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

    def get_absolute_url(self):
        return reverse('users:user_profile', args=[self.id])

    def __str__(self):
        return self.username
