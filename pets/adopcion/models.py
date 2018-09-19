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

class Contratos(models.Model):
    fecha = models.DateTimeField()
    adjunto = models.CharField(max_length=250)
    estado = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.fecha

class TipoRelacion(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre

class Relacion(models.Model):
    usuario = models.ForeignKey(OwnerProfile, models.DO_NOTHING, db_column='usuario', primary_key=True)
    mascota = models.ForeignKey(Pet, models.DO_NOTHING, db_column='mascota')
    fecha = models.DateTimeField()
    tipo_relacion = models.ForeignKey('TipoRelacion', models.DO_NOTHING, db_column='tipo_relacion')
    contratos = models.ForeignKey('Contratos', models.DO_NOTHING, db_column='contratos', blank=True, null=True)

    def __str__(self):
        return self.tipo_relacion.nombre

    class Meta:
        managed = False
        unique_together = (('usuario', 'mascota'),)

    def get_contratos(self):
        return self.contratos.fecha

class Seguimiento(models.Model):
    contratos = models.ForeignKey('Contratos', models.DO_NOTHING, db_column='contratos')
    fecha = models.DateTimeField()
    observaciones = models.CharField(max_length=250, blank=True, null=True)
    adjuntos = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.fecha

class Visitas(models.Model):
    contratos = models.ForeignKey('Contratos', models.DO_NOTHING, db_column='contratos')
    fecha_visita = models.DateTimeField()
    fecha_prox_visita = models.DateTimeField(blank=True, null=True)
    observaciones = models.CharField(max_length=250)
    adjuntos = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.fecha

