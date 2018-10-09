from django.core.exceptions import ValidationError

def validate_cc(value):
    msg = 'Por favor ingrese una cedula de ciudadania valida'
    if 'www.facebook.com/' not in value and 'www.fb.com' not in value:
        raise ValidationError(msg)
