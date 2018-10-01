from django.conf.urls import url
from django.contrib.auth.views import LogoutView

from . import views, admin_views

from users.admin import AdminFundacion
from django.contrib import admin
#admin.autodiscover()

from .admin_views import (
    OwnerProfileList,
    OwnerProfileDetail,
    OwnerProfileCreation,
    OwnerProfileUpdate,
    OwnerProfileDelete,

    PostulanteList,

    ContratoList,
    IniciarContrato
)

urlpatterns = [
    
    #url(r'^$fundacion', views.CreateFundacionView.as_view(), name='createFundacion'), 
    #url(r'^blabla$', admin_views.report),
    #url(r'^fundacion-admin/$', AdminFundacion.urls),
    url(r'^$', views.SelectCreate, name='createSelect'), 
    
    url(r'^normal$', views.CreateUserView.as_view(), name='create'),
    url(r'^fundacion$', views.CreateFundacionView, name='createFundacion'),
    url(r'^profile/(?P<pk>[0-9]+)/$', views.ProfileDetailView.as_view(), name='user_profile'),
    url(r'^profile/$', views.UserProfileView.as_view(), name='profile'),
    url(r'^profile/edit/$', views.EditUserProfileView.as_view(), name='edit'), 
    url(r'^profile/edit_fundacion/$', views.EditFundacionProfileView.as_view(), name='edit_fundacion'),
    url(r'^login/$', views.UserLogin.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^confirm/$', views.confirm_information, name='confirm_information'),
    url(r'^recover/$', views.RecoverView.as_view(), name='recover_password'),
    url(r'^recover/reset/done/$', views.RecoverResetDoneView.as_view(), name='recover_password_done'),
    url(r'^recover/reset/(?P<token>.+)/$', views.RecoverResetView.as_view(), name='recover_password_reset'),
    url(r'^recover/(?P<signature>.+)/$', views.RecoverDoneView.as_view(), name='recover_password_sent'),

    #Urls para el crud
    url(r'^administrador/$', OwnerProfileList.as_view(), name='f_list'),
    
    url(r'^(?P<pk>\d+)$', OwnerProfileDetail.as_view(), name='f_detail'),
    url(r'^nuevo$', OwnerProfileCreation.as_view(), name='f_new'),
    url(r'^editar/(?P<pk>\d+)$', OwnerProfileUpdate.as_view(), name='f_edit'),
    url(r'^borrar/(?P<pk>\d+)$', OwnerProfileDelete.as_view(), name='f_delete'),

    url(r'^administrador/postulantes$', PostulanteList.as_view(), name='r_list'),

    url(r'^contratos/list$', ContratoList.as_view(), name='c_list'),

    url(r'^contratos/(?P<m>(\d+))/(?P<u>(\d+))/$', IniciarContrato, name='c_new'),
    #url(r'^contrato/(?P<pk>\d+)$', ContratoCreation.as_view(), name='c_new'),
]
