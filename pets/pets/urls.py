from django.conf import settings
from django.conf.urls import include, url, static
from django.contrib import admin

#app_name = 'meupet'
#urlpatterns = [
    #url(r'^pets/', include('meupet.urls', namespace='meupet')),
#    url(r'^pets/', include(('meupet.urls', 'meupet'), namespace='meupet')),
    #path(r'^pets/', include('meupet.urls', namespace='meupet')),
#    url(r'^social/', include('social_django.urls', namespace='social')),
#    url(r'^user/', include('users.urls', namespace='users')),
#    url(r'^api/', include('api.urls', namespace='api')),
#    url(r'^admin/', include(admin.site.urls)),
#    url(r'^', include('common.urls', namespace='common')),
#]
#admin.autodiscover()
urlpatterns = [
    url(r'^pets/', include(('meupet.urls', 'meupet'), namespace='meupet')),
    url(r'^social/', include(('social_django.urls', 'social'), namespace='social')),
    url(r'^user/', include(('users.urls', 'users'), namespace='users')),
    url(r'^api/', include(('api.urls', 'api'), namespace='api')),
    url(r'^', include(('common.urls', 'common'), namespace='common')),
    url(r'^adopcion/', include(('adopcion.urls', 'adopcion'), namespace='adopcion')),
    url(r'^admin/', admin.site.urls),
]



if settings.DEBUG:
    urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
