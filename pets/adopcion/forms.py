from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from users.models import OwnerProfile

class PostForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(PostForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['tipo_identificacion'].required = True
		self.fields['num_identificacion'].required = True
		self.fields['first_name'].required = True
		self.fields['last_name'].required = True
		self.fields['email'].required = True
		self.fields['phone'].required = True
		#atreem
		self.fields['tipo_identificacion'].widget.attrs.update({'class': 'form-control'})
		self.fields['num_identificacion'].widget.attrs.update({'class': 'form-control'})
		self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
		self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
		self.fields['email'].widget.attrs.update({'class': 'form-control'})
		self.fields['phone'].widget.attrs.update({'class': 'form-control'})

	class Meta:
		model = OwnerProfile
		fields = ('tipo_identificacion','num_identificacion','first_name', 'last_name','email','phone',)
		#fields = ('first_name', 'last_name', 'email',)
		#fields['first_name'].widget.attrs.update({'class': 'form-control'})
        #self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        #self.fields['email'].widget.attrs.update({'class': 'form-control'})	