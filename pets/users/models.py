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
    tipo_identificacion = models.CharField(max_length=2,
                            choices=TIPO_ID,
                            blank=True)
    num_identificacion = models.IntegerField('Numero de identificación',unique=True,validators=[MinValueValidator(11111111)])
    is_information_confirmed = models.BooleanField(default=False)
    facebook = models.URLField(max_length=250, blank=True, null=True,
                               validators=[validate_facebook_url])
    phone = models.CharField('Telefono de contacto',  max_length=30, blank=True)

    def get_absolute_url(self):
        return reverse('users:user_profile', args=[self.id])

    def __str__(self):
        return self.username
