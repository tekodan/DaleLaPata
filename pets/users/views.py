from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy
from django.http.response import HttpResponseRedirect
from django.shortcuts import resolve_url
from django.utils.translation import ugettext as _
from django.views.generic import CreateView, TemplateView, UpdateView, DetailView
from password_reset.views import Recover, RecoverDone, Reset, ResetDone

from users.forms import LoginForm, RegisterForm, UpdateUserForm, UsersPasswordRecoveryForm, UsersPasswordResetForm, RegisterFormFund
from users.models import OwnerProfile, MyFundacion
from django.shortcuts import render

def SelectCreate(request):
    return render(request, 'users/SelectCreate.html')


class RecoverView(Recover):
    template_name = 'users/recover.html'
    form_class = UsersPasswordRecoveryForm
    success_url_name = 'users:recover_password_sent'
    email_template_name = 'users/recover_email.txt'
    search_fields = ['username', 'email']


class RecoverDoneView(RecoverDone):
    template_name = 'users/recover.html'


class RecoverResetView(Reset):
    template_name = 'users/reset.html'
    success_url = 'users:recover_password_done'
    form_class = UsersPasswordResetForm
    token_expires = 3600 * 2


class RecoverResetDoneView(ResetDone):
    template_name = 'users/reset_done.html'


class CreateUserView(CreateView):
    model = OwnerProfile
    form_class = RegisterForm
    template_name = 'users/create.html'
    authenticated_redirect_url = reverse_lazy('meupet:index')

    msg = _('Su cuenta ha sido creada, Accede <a href="{0}">'
            'a esta pagina</a> y registra a muchos amigos :)')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(resolve_url(self.authenticated_redirect_url))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.is_information_confirmed = True
        return super(CreateUserView, self).form_valid(form)

    def get_success_url(self):
        url = reverse('meupet:register')
        messages.success(self.request, self.msg.format(url))
        user = authenticate(
            username=self.request.POST.get('username'),
            password=self.request.POST.get('password1')
        )
        login(self.request, user)
        return reverse('meupet:index')

def _get_form(request, formcls, prefix):
    #data = request.POST if prefix in request.POST else None
    data = request.POST if prefix in next(iter(request.POST.keys())) else None
    return formcls(data, prefix=prefix)

def CreateFundacionView(request):
    #log = logging.getLogger(__name__)
    if request.method == "POST":

        form = RegisterFormFund(request.POST)
        if form.is_valid():

            MyFundacion = form.save()
            #log.info("ENTRO fundacion")
            #return redirect(reverse('users:create_user',kwargs={'pk': MyFundacion.id}))
            return render(request, 'users/doneFundacion.html', {'form': form})
            #return render(request, 'users/create_fundacion.html', {'form': form})
        else:
            return render(request, 'users/create_fundacion.html', {'form': form})

    else:
        form = RegisterFormFund()
        return render(request, 'users/create_fundacion.html', {'form': form})


class EditUserProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'users/edit_profile.html'
    model = OwnerProfile
    form_class = UpdateUserForm

    def get_success_url(self):
        messages.success(self.request, _('Changes saved successfully.'))
        return reverse('meupet:index')

    def get_object(self, queryset=None):
        return self.request.user


class UserLogin(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'
    #MyFundacion.objects.get(self.request.user.fundacion)
    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['object'] = self.request.user
        context['fundacion'] = self.request.user.fundacion
        context['pets'] = self.request.user.pet_set.all()
        return context


class ProfileDetailView(DetailView):
    template_name = 'users/profile.html'
    model = OwnerProfile

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        context['pets'] = self.object.pet_set.all()
        context['fundacion'] = self.request.user.fundacion
        return context


def confirm_information(request):
    """ This check that the user has confirmed the information and
    redirect to the correct view"""
    if request.user:
        if request.user.is_information_confirmed:
            return HttpResponseRedirect(reverse('meupet:index'))
        else:
            return HttpResponseRedirect(reverse('users:edit'))
