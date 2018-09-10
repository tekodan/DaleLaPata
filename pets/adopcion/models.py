# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from meupet.models import Pet
from users.models import OwnerProfile
from django.utils.translation import ugettext_lazy as _

class MyContratos(models.Model):
    fecha = models.DateTimeField()
    adjunto = models.CharField(max_length=250)
    estado = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my_contratos'

class MyTipoRelacion(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'my_tipo_relacion'

class MyRelacion(models.Model):
    usuario = models.ForeignKey(OwnerProfile, models.DO_NOTHING, db_column='usuario', primary_key=True)
    mascota = models.ForeignKey(Pet, models.DO_NOTHING, db_column='mascota')
    fecha = models.DateTimeField()
    tipo_relacion = models.ForeignKey('MyTipoRelacion', models.DO_NOTHING, db_column='tipo_relacion')
    contratos = models.ForeignKey('MyContratos', models.DO_NOTHING, db_column='contratos', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my_relacion'
        unique_together = (('usuario', 'mascota'),)

    def get_contratos(self):
        return self.contratos.fecha

class MySeguimiento(models.Model):
    contratos = models.ForeignKey('MyContratos', models.DO_NOTHING, db_column='contratos')
    fecha = models.DateTimeField()
    observaciones = models.CharField(max_length=250, blank=True, null=True)
    adjuntos = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my_seguimiento'

class MyVisitas(models.Model):
    contratos = models.ForeignKey('MyContratos', models.DO_NOTHING, db_column='contratos')
    fecha_visita = models.DateTimeField()
    fecha_prox_visita = models.DateTimeField(blank=True, null=True)
    observaciones = models.CharField(max_length=250)
    adjuntos = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my_visitas'

class MyFundacion(models.Model):
    RUT = 'RUT'
    NIT = 'NIT'
    TIPO_ID = (
        (RUT, _('RUT')),
        (NIT, _('NIT')),
    )
    tipo_identificacion = models.CharField(max_length=3,
                                           choices=TIPO_ID,
                                           blank=True)
    numero_identificacion = models.CharField(unique=True,max_length=15)
    razon_social = models.CharField(max_length=250, blank=True, null=True)
    fecha_fundacion = models.DateTimeField(blank=True, null=True)
    email = models.CharField(unique=True, max_length=250, blank=True, null=True)
    telefono = models.CharField(max_length=250, blank=True, null=True)
    logo = models.ImageField(upload_to='fundacion_profiles',
                                        help_text=_('Maximo tamaño de imagen 8mb'))
    facebook = models.URLField(max_length=250, blank=True, null=True,
                               validators=[])
    twitter = models.URLField(max_length=250, blank=True, null=True,
                               validators=[])
    contrato_base = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my_fundacion'