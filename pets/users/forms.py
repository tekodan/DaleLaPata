from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from password_reset.forms import PasswordRecoveryForm, PasswordResetForm

from users.models import OwnerProfile, Fundacion


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'autofocus': 'autofocus'})
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})


class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
        #self.fields['fundacion'].required = True
        #self.fields['rol'].required = True
        #self.fields['tipo_identificacion'].required = True
        #self.fields['num_identificacion'].required = True
        self.fields['facebook'].help_text = _(
            'Click <a href="#" data-toggle="modal" data-target="#ajuda-facebook">'
            'Aqui</a> para obtener ayuda como llenar este campo.')
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})

class FundacionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FundacionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['nombre_corto'].widget.attrs.update({'class': 'form-control'})
        self.fields['razon_social'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['telefono'].widget.attrs.update({'class': 'form-control'})
        self.fields['logo'].widget.attrs.update({'class': 'form-control'})
        self.fields['facebook'].widget.attrs.update({'class': 'form-control'})
        self.fields['twitter'].widget.attrs.update({'class': 'form-control'})
        #self.fields['contrato_base'].widget.attrs.update({'class': 'form-control'})

def _build_choice_field(label, choices=None, required=False):
    empty_choice = (('', '------------'),)
    field = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        label=label,
        choices=empty_choice,
        required=required
    )
    if choices:
        field.choices += choices
    return field

class RegisterForm(UserForm):
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Password confirmation'), widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['facebook'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
        self.fields['facebook'].widget.attrs.update(
            {'placeholder': _('Ingresa la url completa de su perfil en facebook.')})

        self.fields['username'].help_text = _('Requerido 30 caracteres o menos. '
                                              'Solo letras, numeros y @/./+/-/_.')
        self.fields['fundacion'].widget.attrs.update({'class': 'form-control'})

        #self.fields['rol'] = _build_choice_field(_('Rol'), required=True)
        #self.fields['rol']: forms.Select(attrs={'class': 'form-control'})
        self.fields['rol'].widget.attrs.update({'class': 'form-control'})

        #self.fields['tipo_identificacion']: forms.Select(attrs={'class': 'form-control'})
        self.fields['tipo_identificacion'].widget.attrs.update({'class': 'form-control'})
        self.fields['num_identificacion'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = OwnerProfile
        fields = ('first_name', 'last_name', 'email', 'username',
                  'facebook', 'phone', 'password1', 'password2', 'fundacion', 
                  'rol', 'tipo_identificacion', 'num_identificacion')


    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("The two password fields didn't match."))
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class RegisterFormFund(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RegisterFormFund, self).__init__(*args, **kwargs)
        self.fields['tipo_identificacion'].widget.attrs.update({'class': 'form-control'})
        self.fields['num_identificacion'].widget.attrs.update({'class': 'form-control'})
        self.fields['nombre_corto'].widget.attrs.update({'class': 'form-control'})
        self.fields['razon_social'].widget.attrs.update({'class': 'form-control'})
        self.fields['fecha_fundacion'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['telefono'].widget.attrs.update({'class': 'form-control'})
        self.fields['logo'].widget.attrs.update({'class': 'form-control'})
        self.fields['facebook'].widget.attrs.update({'class': 'form-control'})
        self.fields['twitter'].widget.attrs.update({'class': 'form-control'})
        #self.fields['contrato_base'].widget.attrs.update({'class': 'form-control'})
        self.fields['facebook'].widget.attrs.update(
            {'placeholder': _('Ingrese la direccion completa de su usuario en Facebook')})

    class Meta:
        model = Fundacion
        fields = ('tipo_identificacion', 'num_identificacion', 'nombre_corto', 'razon_social', 'fecha_fundacion',
                  'email', 'telefono', 'logo', 'facebook','twitter',)

class UpdateFundacionForm(FundacionForm):
    class Meta:
        model = Fundacion
        fields = ('nombre_corto','razon_social', 'email', 'telefono', 'logo', 'facebook', 'twitter',)

    def __init__(self, *args, **kwargs):
        super(UpdateFundacionForm, self).__init__(*args, **kwargs)
        self.helper.add_input(Submit('submit', _('Save Changes')))

    def save(self, commit=True):
        self.instance.is_information_confirmed = True
        super(UpdateFundacionForm, self).save()
        

class UpdateUserForm(UserForm):
    class Meta:
        model = OwnerProfile
        fields = ('first_name', 'last_name', 'email', 'facebook', 'phone',)

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        self.helper.add_input(Submit('submit', _('Save Changes')))

    def save(self, commit=True):
        self.instance.is_information_confirmed = True
        super(UpdateUserForm, self).save()


class UsersPasswordRecoveryForm(PasswordRecoveryForm):
    def __init__(self, *args, **kwargs):
        super(UsersPasswordRecoveryForm, self).__init__(*args, **kwargs)
        self.fields['username_or_email'].label = ''
        self.helper = FormHelper()
        self.helper.add_input(Submit('recover', _('Recover password')))


class UsersPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UsersPasswordResetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('recover', _('Recover password')))
