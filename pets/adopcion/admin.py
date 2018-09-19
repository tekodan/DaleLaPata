from django.contrib import admin

# Register your models here.
from adopcion import models

admin.site.register(models.Contratos)
admin.site.register(models.TipoRelacion)
admin.site.register(models.Relacion)
admin.site.register(models.Seguimiento)
admin.site.register(models.Visitas)
