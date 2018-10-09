from django.shortcuts import render
from django.views.generic import TemplateView
from meupet.views import render_pet_list,pet_list
from meupet import forms, models
from django.views.generic import (ListView)


class AboutPageView(TemplateView):
    template_name = 'staticpages/about.html'
    context_object_name = 'pets'

class PetIndexHome(ListView):
    template_name = 'common/home.html'
    context_object_name = 'pets'

    def get_queryset(self):
        return models.Pet.objects.select_related('city').order_by('-id')[:12]
