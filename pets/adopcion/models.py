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

class Contratos_Fundacion(models.Model):
    E_01 = '1'
    E_02 = '2'
    E_03 = '3'
    ESTADO = (
        (E_01, _('Concertado')),
        (E_02, _('Pendiente')),
        (E_03, _('Anulado')),
    ) 
    objeto = models.CharField(max_length=250)   
    fecha = models.DateTimeField()
    observaciones = models.CharField(max_length=1000)
    estado = models.CharField(max_length=1, choices=ESTADO)

    def __str__(self):
        return self.objeto

class Adjuntos_Contratos_Fundacion(models.Model):
    contrato = models.ForeignKey(Contratos_Fundacion, models.DO_NOTHING, db_column='contrato')
    adjunto = models.ImageField(upload_to='fundacion_contratos',
                                        help_text=_('Maximo tamaño de imagen 8mb'))

    def __str__(self):
        return self.id

class ContratoBase(models.Model):
    nombre = models.CharField(max_length=250)
    fecha_agregado = models.DateTimeField()
    descripcion = models.TextField(max_length=2000)
    observaciones = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.nombre

class Clausulas_Base(models.Model):
    contrato = models.ForeignKey(ContratoBase, models.DO_NOTHING, db_column='contrato_base')
    nombre = models.CharField(max_length=250)
    fecha_agregado = models.DateTimeField()
    descripcion = models.TextField(max_length=2000)
    observaciones = models.CharField(max_length=1000,blank=True, null=True)

    def __str__(self):
        return self.nombre

class Clausulas_Fundacion(models.Model):
    E_01 = '1'
    E_02 = '2'
    E_03 = '3'
    ESTADO = (
        (E_01, _('Aprobada')),
        (E_02, _('Pendiente')),
        (E_03, _('Anulada')),
    )
    T_01 = '1'
    T_02 = '2'
    TIPO = (
        (T_01, _('Adicional')),
        (T_02, _('Anulada')),
    )
    nombre = models.CharField(max_length=250)
    fecha_agregado = models.DateTimeField()
    descripcion = models.TextField(max_length=2000)
    observaciones = models.CharField(max_length=1000,blank=True, null=True)
    estado = models.CharField(max_length=1, choices=ESTADO)

    def __str__(self):
        return self.nombre

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
    contratos = models.ForeignKey('Contratos_Fundacion', models.DO_NOTHING, db_column='Contratos_Fundacion', blank=True, null=True)

    class Meta:
        unique_together = ('usuario', 'mascota')

    def __str__(self):
        return self.tipo_relacion.nombre+str(' - ')+self.usuario.first_name+str(' & ')+self.mascota.name

class Seguimiento(models.Model):
    contratos = models.ForeignKey('Contratos_Fundacion', models.DO_NOTHING, db_column='Contratos_Fundacion')
    fecha = models.DateTimeField()
    observaciones = models.CharField(max_length=250, blank=True, null=True)
    adjuntos = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.fecha

class Visitas(models.Model):
    contratos = models.ForeignKey('Contratos_Fundacion', models.DO_NOTHING, db_column='Contratos_Fundacion')
    fecha_visita = models.DateTimeField()
    fecha_prox_visita = models.DateTimeField(blank=True, null=True)
    observaciones = models.CharField(max_length=250)
    adjuntos = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.fecha

