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

from adopcion.models import Relacion

from django.shortcuts import get_list_or_404, get_object_or_404

class OwnerProfileList(ListView):
    model = OwnerProfile
    #template_name="users/ownerprofile_list.html"

    def get_queryset(self, *args, **kwargs):
        qs = OwnerProfile.objects.all()
        qs = qs.filter(fundacion=self.request.user.fundacion)
        return qs

class PostulanteList(ListView):
    model = Relacion
    #template_name="users/ownerprofile_list.html"

    def get_queryset(self, *args, **kwargs):
        qs = Relacion.objects.filter(mascota__fundacion=self.request.user.fundacion)
        return qs

class OwnerProfileDetail(DetailView):
    model = OwnerProfile

class OwnerProfileCreation(CreateView):
    model = OwnerProfile
    success_url = reverse_lazy('users:f_list')
    fields = ['tipo_identificacion', 'num_identificacion', 'first_name', 'last_name', 'username','email', 'phone', 'facebook']

class OwnerProfileUpdate(UpdateView):
    model = OwnerProfile
    success_url = reverse_lazy('users:f_list')
    fields = ['first_name', 'last_name', 'email', 'phone', 'facebook']

class OwnerProfileDelete(DeleteView):
    model = OwnerProfile
    success_url = reverse_lazy('users:f_list')

