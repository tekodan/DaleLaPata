from django.contrib import admin

# Register your models here.
from adopcion import models

admin.site.register(models.Contratos_Fundacion)
admin.site.register(models.ContratoBase)
admin.site.register(models.Clausulas_Base)
admin.site.register(models.TipoRelacion)
admin.site.register(models.Relacion)
admin.site.register(models.Seguimiento)
admin.site.register(models.Visitas)
