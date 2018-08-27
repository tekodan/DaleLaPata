# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
