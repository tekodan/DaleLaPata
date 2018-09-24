from django.contrib import admin

from users.models import OwnerProfile, Fundacion


class OwnerProfileAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'first_name',
        'last_name',
        'date_joined',
        'last_login',
        #'is_information_confirmed',
        'fundacion',
    )
    list_filter = (
        'date_joined',
        'last_login',
        'is_information_confirmed'
    )

    #cuando es superusuario muestra todos los users, cuando no, solo los de su fundacion
    def get_queryset(self, request):        
        query = super(OwnerProfileAdmin, self).get_queryset(request)
        filtered_query = query.filter() 
        if not request.user.is_superuser :
            filtered_query = query.filter(fundacion=request.user.fundacion.id)  
            #exclude = ('is_superuser',)
        return filtered_query

    #def __init__( self, request,):
    #   if not request.user.is_superuser :
    #        exclude = ('is_superuser', 'is_staff',)

class FundacionAdmin(admin.ModelAdmin):
    #actions_on_bottom = False
    #cuando es superusuario muestra todos las fundaciones, cuando no, solo su fundacion
    def get_queryset(self, request):        
        query = super(FundacionAdmin, self).get_queryset(request)
        filtered_query = query.filter() 
        if not request.user.is_superuser :
            filtered_query = query.filter(id=request.user.fundacion.id)  
            #exclude = ('is_superuser',)
        return filtered_query

    #si no es superusuario se deshabilita añadir fundacion    
    def has_add_permission(self, request, obj=None):
        if not request.user.is_superuser :
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        if not request.user.is_superuser :
            return False
        return True

admin.site.register(OwnerProfile, OwnerProfileAdmin)
admin.site.register(Fundacion, FundacionAdmin)

#segundo admin
"""
from django.contrib.admin import AdminSite
from django.contrib.auth.models import Permission


from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.utils.translation import ugettext_lazy

class UserAdminAuthenticationForm(AuthenticationForm):
    this_is_the_login_form = forms.BooleanField(widget=forms.HiddenInput,
                                initial=1,
                                error_messages={'required': ugettext_lazy(
                                "Please log in again, because your session has"
                                " expired.")})

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        message = ERROR_MESSAGE

        if username and password:
            self.user_cache = authenticate(username=username,
            password=password)
            if self.user_cache is None:
                if u'@' in username:
                    # Mistakenly entered e-mail address instead of username?
                    # Look it up.
                    try:
                        user = User.objects.get(email=username)
                    except (User.DoesNotExist, User.MultipleObjectsReturned):
                        # Nothing to do here, moving along.
                        pass
                    else:
                        if user.check_password(password):
                            message = _("Your e-mail address is not your "
                                        "username."
                                        " Try '%s' instead.") % user.username
                raise forms.ValidationError(message)
            # Removed check for is_staff here!
            elif not self.user_cache.is_active:
                raise forms.ValidationError(message)
        self.check_for_test_cookie()
        return self.cleaned_data

class AdminFundacion(AdminSite):
    #site_header = "Administracion de fundación"
    #site_title = "Bienvenido a la gestion de "
    #index_title = "Bienvenido a la gestion de"

    login_form = UserAdminAuthenticationForm

    def has_permission(self, request):
        if request.user.is_active : 
            if request.user.rol=='1' :
                self.index_title="Bienvenido a la gestion de "+str(request.user.fundacion)              
                #pl = Permission.objects.filter(codename__in=["view_fundacion","change_fundacion"])
                #request.user.user_permissions.add(*pl)
                return request.user.is_active


class FundacionAdmin(admin.ModelAdmin):

    def get_queryset(self, request):        
        query = super(FundacionAdmin, self).get_queryset(request)
        filtered_query = query.filter(id=request.user.fundacion.id)             
        return filtered_query

class UserAdmin(admin.ModelAdmin):
    def get_queryset(self, request):        
        query = super(UserAdmin, self).get_queryset(request)
        filtered_query = query.filter(fundacion=request.user.fundacion.id)             
        return filtered_query

fundacion_admin_site = AdminFundacion(name='fundacion-admin')
fundacion_admin_site.register(Fundacion,FundacionAdmin)
#fundacion_admin_site.register(OwnerProfile,UserAdmin)
"""

