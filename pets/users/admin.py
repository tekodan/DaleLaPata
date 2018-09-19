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


admin.site.register(OwnerProfile, OwnerProfileAdmin)
admin.site.register(Fundacion)
