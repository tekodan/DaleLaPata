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
    BASE = '1'
    PERSONALIZADO = '2'
    TIPO = (
        (BASE, _('Base')),
        (PERSONALIZADO, _('Personalizado')),
    )  
    ADOPCIÓN = '1'
    HOGAR = '2'
    APADRINAMIENTO = '2'
    OBJETO = (
        (ADOPCIÓN, _('Adopción')),
        (HOGAR, _('Hogar de paso')),
        (APADRINAMIENTO, _('Apadrinamiento')),
    )  
    nombre = models.CharField(max_length=250)
    objeto = models.CharField(max_length=1, choices=OBJETO)   
    fecha_creacion = models.DateTimeField()
    descripcion = models.TextField()
    observaciones = models.TextField(blank=True, null=True)
    tipo = models.CharField(max_length=1, choices=TIPO)
    contrato_base = models.ForeignKey('self', blank=True, null=True, on_delete=models.PROTECT)
    fundacion = models.ForeignKey('users.Fundacion', models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Clausulas(models.Model):
    BASE = '1'
    PERSONALIZADO = '2'
    TIPO = (
        (BASE, _('Base')),
        (PERSONALIZADO, _('Personalizado')),
    )  
    nombre = models.CharField(max_length=250)
    fecha_creacion = models.DateTimeField()
    descripcion = models.TextField()
    observaciones = models.TextField(blank=True, null=True)
    tipo = models.CharField(max_length=1, choices=TIPO)
    contrato = models.ForeignKey('Contratos', models.DO_NOTHING)

    def __str__(self):
        return self.nombre

class TipoRelacion(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=500)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Relacion(models.Model):
    usuario = models.ForeignKey(OwnerProfile, models.DO_NOTHING, db_column='usuario')
    mascota = models.ForeignKey(Pet, models.DO_NOTHING, db_column='mascota')
    fecha = models.DateTimeField()
    tipo_relacion = models.ForeignKey('TipoRelacion', models.DO_NOTHING, db_column='tipo_relacion')
 
    class Meta:
        unique_together = ('usuario', 'mascota')

    def __str__(self):
        return self.tipo_relacion.nombre+str(' - ')+self.usuario.first_name+str(' & ')+self.mascota.name

class Seguimiento(models.Model):
    EVIDENCIA = '1'
    VISITA = '2'
    CONTRATO = '3'
    TIPO = (
        (EVIDENCIA, _('Evidencia')),
        (VISITA, _('Visita')),
        (CONTRATO, _('Contrato')),
    ) 
    APROBACIÓN = '1'
    ANULACIÓN = '2'
    PENDIENTE = '3'
    ANOMALIAS = '4'
    ESTADO = (
        (APROBACIÓN, _('Aprobación')),
        (ANULACIÓN, _('Anulación')),
        (PENDIENTE, _('Pendiente')),
        (ANOMALIAS, _('Anomalias')),
    ) 
    tipo = models.CharField(max_length=1, choices=TIPO)
    estado = models.CharField(max_length=1, choices=ESTADO)
    fecha = models.DateTimeField()
    descripcion = models.TextField(max_length=2000)
    observaciones = models.TextField(max_length=2000, blank=True, null=True)
    anterior = models.OneToOneField('self', blank=True, null=True, on_delete=models.PROTECT)
    relacion = models.ForeignKey('Relacion', models.DO_NOTHING)

    def __str__(self):
        return self.fecha

class Adjuntos_Seguimiento(models.Model):
    """
    CHOICES = (
        ('Evidencia', ((1, 'Aprobación'), (2, 'Anulación'), (3, 'Anomalias'))),
        ('Visita', ((4, 'Aprobación'), (5, 'Anomalias'), (6, '6'))),
        ('Contrato', ((4, 'Aprobación'), (5, 'Anulación'), (6, 'Pendiente'))),
    )

    # Just the letters: (('A', 'A'), ('B', 'B'))
    LETTER_CHOICES = tuple((l[0], l[0]) for l in CHOICES)

    letter = models.CharField(max_length=1, choices=LETTER_CHOICES)
    number = models.PositiveIntegerField(max_length=1, choices=CHOICES)
    """
    seguimiento = models.ForeignKey(Seguimiento, models.DO_NOTHING)
    adjunto = models.ImageField(upload_to='relacion_seguimiento',
                                        help_text=_('Maximo tamaño de imagen 8mb'))

    def __str__(self):
        return self.id

