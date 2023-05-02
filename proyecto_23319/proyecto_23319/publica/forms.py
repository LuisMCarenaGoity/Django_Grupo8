from django import forms;


from django.forms import ValidationError;
import re

def solo_caracteres(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('El nombre no puede contener números. %(valor)s',
                            code='Invalid',
                            params={'valor':value})
def validate_email(value):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, value):
        raise ValidationError('Correo electrónico inválido')
    return value

class ContactoForm(forms.Form):
    #TIPO_CONSULTA=(
      #  ('','-seleccione-'),
        #(1,'ejemplo1'),
        #(2,'ejemplo2'),
        #(3,'ejemplo3'),
   # ) ejemplo de un campo select
    nombre = forms.CharField ( label  ='', 
            max_length=50,
            validators=(solo_caracteres,),
            widget=forms.TextInput(
                    attrs={'class':'input',
                        'placeholder':'Nombre'}
                    ))
    email = forms.EmailField(
            label='',
            max_length=100,
            required=False,
            validators=(validate_email,),
            error_messages={
                    'required': 'Por favor completa el campo'
                },
            widget=forms.TextInput(attrs={'class':'input','type':'email','placeholder':'Email'})
        )
    asunto = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={'class':'input','placeholder':'Asunto'})
    )
    mensaje = forms.CharField(
        label='',
        max_length=500,
        widget=forms.Textarea(attrs={'rows': 5,'class':'input','placeholder':'Mensaje'})
    )      
   # email=forms.EmailField(label='email',max_length=50)
    #asunto=forms.CharField(label='asunto')
   # mensaje=forms.CharField(label='mensaje', max_length=250, required=False)
    #tipo_consulta=forms.ChoiceField(label='elija una opccion', choices=TIPO_CONSULTA)me muestra el select
    #check=forms.BooleanField(label='ejemplo de un check', required=False)
    