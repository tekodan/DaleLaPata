# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class MyFundacion(models.Model):
    numero_identificacion = models.IntegerField(unique=True)
    razon_social = models.CharField(max_length=250, blank=True, null=True)
    fecha_fundacion = models.DateTimeField(blank=True, null=True)
    email = models.CharField(unique=True, max_length=250, blank=True, null=True)
    telefono = models.CharField(max_length=250, blank=True, null=True)
    logo = models.CharField(max_length=250, blank=True, null=True)
    contrato_base = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my_fundacion'
