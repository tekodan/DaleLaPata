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
from adopcion.forms import ContratoForm
from users.forms import UpdateUserForm

from django.shortcuts import render

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
        tipor = TipoRelacion.objects.get(nombre__contains = 'Postula')  
        if not self.request.user.is_superuser:
            qs = Relacion.objects.filter(mascota__fundacion=self.request.user.fundacion, tipo_relacion = tipor)
            return qs
        return qs

    def get_context_data(self, **kwargs):
        context = super(PostulanteList, self).get_context_data(**kwargs)
        context['object'] = self.request.user
        return context
##############################################
def IniciarContrato(request, m, u):
    relacion=Relacion.objects.get(mascota=m, usuario=u)
    seguimiento=Seguimiento.objects.get(relacion=relacion)
    if request.method == "POST":

        form = ContratoForm(request.POST)    
        if form.is_valid():
            #seguimiento = form.save(commit=False)  
            seguimiento.descripcion = form.cleaned_data['descripcion']
            seguimiento.observaciones = form.cleaned_data['observaciones']

            relacion.cambiar_adopcion()
            relacion.mascota.change_status()            

            seguimiento.relacion = relacion
            seguimiento.tipo = 3
            seguimiento.estado = 1
            seguimiento.save()
           
            return render(request, 'adopcion/adopcion_done.html', {'relacion':relacion , 'seguimiento':seguimiento})
        else:
            return render(request, 'adopcion/contrato.html', {'form': form , 'relacion':relacion , 'seguimiento':seguimiento})
           
    else:
        form = ContratoForm()
        return render(request, 'adopcion/contrato.html', {'form': form , 'relacion':relacion, 'seguimiento':seguimiento})
##############################################
def GenerarContrato(request, r):
    if request.method == "POST":
        relacion=Relacion.objects.get(id=int(r))        
        return render(request, 'adopcion/contrato_template.html', {'relacion': relacion})           
    else:
        form = ContratoForm()
        return render(request, 'adopcion/contrato.html', {'form': form})
    
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

