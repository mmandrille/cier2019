from django.conf.urls import url
from django.urls import path
#Import de modulos personales
from . import views

app_name = 'calendario'
urlpatterns = [
    url('', views.calendario, name='calendario'),
]