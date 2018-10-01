from users.models import OwnerProfile, Fundacion
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

from adopcion.models import *

from django.shortcuts import get_list_or_404, get_object_or_404
##############################################
class OwnerProfileList(ListView):
    model = OwnerProfile
    #template_name="users/ownerprofile_list.html"

    def get_queryset(self, *args, **kwargs):   
        qs=OwnerProfile.objects.all()
        if not self.request.user.is_superuser:
            qs = qs.filter(fundacion=self.request.user.fundacion)
            return qs
        return qs

    def get_context_data(self, **kwargs):
        context = super(OwnerProfileList, self).get_context_data(**kwargs)
        context['object'] = self.request.user
        return context
##############################################
class PostulanteList(ListView):
    model = Relacion

    def get_queryset(self, *args, **kwargs):   
        qs = Relacion.objects.all()     
        if not self.request.user.is_superuser:
            qs = Relacion.objects.filter(mascota__fundacion=self.request.user.fundacion)
            return qs
        return qs

    def get_context_data(self, **kwargs):
        context = super(PostulanteList, self).get_context_data(**kwargs)
        context['object'] = self.request.user
        return context
##############################################
class AdopcionCreation(CreateView):
    model = Relacion
    #success_url = reverse_lazy('users:f_list')
    fields = ['tipo_identificacion', 'num_identificacion', 'first_name', 'last_name', 'username','email', 'phone', 'facebook']
##############################################
class ContratoCreation(CreateView):
    model = Contratos
    success_url = reverse_lazy('users:r_list')
    fields = ['descripcion_base','objeto', 'fecha', 'observaciones']
    
    def get_context_data(self, **kwargs):
        context = super(ContratoCreation, self).get_context_data(**kwargs)
        context['relacion'] = self.request.relacion
        return context
    
##############################################
class ContratoList(ListView):
    model = Contratos

##############################################
class OwnerProfileDetail(DetailView):
    model = OwnerProfile
##############################################
class OwnerProfileCreation(CreateView):
    model = OwnerProfile
    success_url = reverse_lazy('users:f_list')
    fields = ['tipo_identificacion', 'num_identificacion', 'first_name', 'last_name', 'username','email', 'phone', 'facebook']
##############################################
class OwnerProfileUpdate(UpdateView):
    model = OwnerProfile
    success_url = reverse_lazy('users:f_list')
    fields = ['first_name', 'last_name', 'email', 'phone', 'facebook']
##############################################
class OwnerProfileDelete(DeleteView):
    model = OwnerProfile
    success_url = reverse_lazy('users:f_list')

