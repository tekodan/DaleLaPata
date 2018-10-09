from django.contrib import admin

from meupet import models


class PetAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'kind',
        'city',
        'description',
        'status',
        'created',
        'modified',
        'published',
        'request_sent',
        'active',
    )
    list_filter = (
        'status',
        'kind',
        'created',
        'active',
        'city__state',
    )

    #en caso de no ser superusuario solo mostrar las pets correspondientes a su fundacion
    def get_queryset(self, request):        
        query = super(PetAdmin, self).get_queryset(request)
        filtered_query = query.filter() 
        if not request.user.is_superuser :
            filtered_query = query.filter(fundacion=request.user.fundacion.id)  
            #exclude = ('is_superuser',)
        return filtered_query


admin.site.register(models.Pet, PetAdmin)
admin.site.register(models.Kind)
admin.site.register(models.Photo)
admin.site.register(models.PetStatus)
admin.site.register(models.StatusGroup)
