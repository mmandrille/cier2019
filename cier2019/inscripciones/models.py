from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.utils.timezone import now

#Import Personales

#Creamos choices
CATEGORIA = (
        (1, 'ACTIVO'),
        (2, 'ADHERENTE'),
        (3, 'ESTUDIANTE')
    )
TIPO_DOC= (
        (1, 'Documento Nacional de Identidad'),
        (2, 'Cédula de Identidad'),
        (3, 'Libreta de Enrolamiento'),
        (4, 'Libreta Cívica'),
        (5, 'Pasaporte'),
    )

DESTINO = (
        (0, 'Solo a Mi > Prueba'),
        (1, 'Usuarios Registrados'),
        (2, 'Inscriptos'),
        (3, 'Correos Validados'),
        (4, 'Correos Sin Validar > Masivo'),
    )

# Create your models here.
class Inscriptos(models.Model):
    nombres = models.CharField('Nombres', max_length=50)
    apellido = models.CharField('Apellidos', max_length=50)
    tipo_doc = models.IntegerField(choices=TIPO_DOC, default=1)
    num_doc = models.CharField('Numero de Documento', max_length=50)
    institucion = models.CharField('Institucion', max_length=100, blank=True, null=True)
    telefono = models.CharField('Telefono', max_length=20)
    email = models.EmailField('Correo Electronico Personal')
    activo = models.BooleanField('Mail Validado', default=False)
    pagado = models.BooleanField(default=False)
    def __str__(self):
        return(self.nombres + ' ' + self.apellido)

class Mails(models.Model):
    email = models.EmailField('Correo Electronico', blank=True, null=True)
    valido = models.BooleanField(default=False)
    def __str__(self):
        return(self.email)

class Mensajes(models.Model):
    nombre = models.CharField('Nombres', max_length=50)
    destinatarios = models.IntegerField(choices=DESTINO, default=0)
    cantidad = models.IntegerField(default=100)
    programar = models.DateTimeField(default=now)
    titulo = models.CharField('Titulo', max_length=50)
    cuerpo = HTMLField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    enviado = models.BooleanField(default=False)

class Progress_Links(models.Model):
    tarea = models.CharField('Tarea', max_length=50)
    inicio = models.DateTimeField(default=now)
    progress_url = models.URLField('Web', blank=True, null=True)
