from .forms import PostForm
from django.shortcuts import get_object_or_404 , render
from meupet.models import Pet
from adopcion.models import Relacion, TipoRelacion, Seguimiento , Adjuntos_Seguimiento
import logging
from django.utils import timezone
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

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

            s = Seguimiento.objects.create(
            tipo=3,
            estado=4,
            fecha=timezone.now(),
            descripcion='Postulación para mascota, pendiente de celebrar contrato',
            relacion=relacion)
            
            s.save()
            #OwnerProfile.first_name = request.user
            #OwnerProfile.last_name = timezone.now()
            #OwnerProfile.last_name = timezone.now()
            #return redirect('post_detail', pk=post.pk)
            log.info("ENTRO")
            #context['fundacion'] = self.request.user.fundacion
            return render(request, 'adopcion/done.html', {'pet': pet , 'user_name': str(ownerprofile.first_name)+str(' ')+str(ownerprofile.last_name),'form': form})
        else:
            return render(request, 'adopcion/home.html', {'form': form})
           
    else:
        form = PostForm()
        return render(request, 'adopcion/home.html', {'pet_name': pet.name, 'form': form})

def upload_image(request, id):
    r = get_object_or_404(Relacion, id=id)
    s = get_object_or_404(Seguimiento, relacion=r.id, anterior__isnull=True)
    picture = request.FILES.get('another_picture', False)

    if request.method == 'POST' and picture:
        Adjuntos_Seguimiento.objects.create(seguimiento=s, adjunto=picture)

    return HttpResponseRedirect(reverse('users:c_new', kwargs={'m': r.mascota.id, 'u': r.usuario.id}))