#Import Standard
from django.forms import ModelForm
#Import Personales
from .models import Inscriptos

#creamos ModelForm
class InscriptoForm(ModelForm):
    class Meta:
        model = Inscriptos
        fields = ['nombres', 'apellido', 'tipo_doc', 'num_doc', 
                    'institucion', 'telefono', 'email',]