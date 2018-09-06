from django.conf.urls import url
from django.views.generic import RedirectView
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [    
    url(r'^(?P<pk>[-\w]*)/$', views.post_new, name='create'),
    #url(r'^$', views.post_new, name='create'),
]
