from django.contrib import admin

from users.models import OwnerProfile, Fundacion


class OwnerProfileAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'first_name',
        'last_name',
        'date_joined',
        'last_login',
        'is_information_confirmed',
    )
    list_filter = (
        'date_joined',
        'last_login',
        'is_information_confirmed'
    )




#segundo admin
from django.contrib.admin import AdminSite

class AdminFundacion(AdminSite):
    site_header = "Administracion de fundación"
    site_title = "Bienvenido a la gestion de "
    index_title = "Bienvenido a la gestion de"

    def has_permission(self, request):
        return request.user.is_active

class FundacionAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        query = super(FundacionAdmin, self).get_queryset(request)
        filtered_query = query.filter()
        if not request.user.is_superuser :        
            if request.user.is_staff : 
                filtered_query = query.filter(id=request.user.fundacion) 
            
        return filtered_query

fundacion_admin_site = AdminFundacion(name='fundacion-admin')
fundacion_admin_site.register(Fundacion,FundacionAdmin)

admin.site.register(OwnerProfile, OwnerProfileAdmin)
#admin.site.register(Fundacion, FundacionAdmin)