from .forms import PostForm
from django.shortcuts import render
from meupet.models import Pet
from adopcion.models import Relacion, TipoRelacion
import logging
from django.utils import timezone

from django.views.generic import CreateView, TemplateView, UpdateView, DetailView

def post_new(request, pk):
    log=logging.getLogger(__name__)
    pet = Pet.objects.get(id=int(pk))

    if request.method == "POST":

        form = PostForm(request.POST)    
        if form.is_valid():
            ownerprofile = form.save(commit=False)
            ownerprofile.username=ownerprofile.num_identificacion
            ownerprofile.password=12345
            tipor = TipoRelacion.objects.get(nombre='Postulación')

            ownerprofile.save()

            relacion=Relacion()
            relacion.usuario=ownerprofile
            relacion.mascota = pet
            relacion.fecha = timezone.now()
            relacion.tipo_relacion = tipor

            relacion.save()
            #OwnerProfile.first_name = request.user
            #OwnerProfile.last_name = timezone.now()
            #OwnerProfile.last_name = timezone.now()
            #return redirect('post_detail', pk=post.pk)
            log.info("ENTRO")
            #context['fundacion'] = self.request.user.fundacion
            return render(request, 'adopcion/done.html', {'pet_nombre': pet.name, 'pet_slug': pet.slug, 'user_name': str(ownerprofile.first_name)+str(' ')+str(ownerprofile.last_name),'form': form})
        else:
            return render(request, 'adopcion/home.html', {'form': form})
           
    else:
        form = PostForm()
        return render(request, 'adopcion/home.html', {'pet_name': pet.name, 'form': form})