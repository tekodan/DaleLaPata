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

class FundacionList(ListView):
    model = Fundacion


class FundacionDetail(DetailView):
    model = Fundacion


class FundacionCreation(CreateView):
    model = Fundacion
    success_url = reverse_lazy('users:f_list')
    fields = ['tipo_identificacion', 'num_identificacion', 'razon_social', 'fecha_fundacion', 'email', 'telefono', 'logo', 'facebook', 'twitter']

class FundacionUpdate(UpdateView):
    model = Fundacion
    success_url = reverse_lazy('users:f_list')
    fields = ['razon_social', 'fecha_fundacion', 'email', 'telefono', 'logo', 'facebook', 'twitter']

class FundacionDelete(DeleteView):
    model = Fundacion
    success_url = reverse_lazy('users:f_list')


