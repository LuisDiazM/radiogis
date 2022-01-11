from django.urls import path 
from . import views

app_name = "paws"
urlpatterns = [
    path("index", views.index, name="index-paws"),
    path("register", views.register, name="register"),
    path("ayuda-formulario", views.documentacion_registro, name="ayuda"),
    path("avail-spectrum", views.avail_spectrum, name="avail-spectrum"), # para el maestro
    path("dispositivos-validados", views.dispositivos_validados, name="dispositivos-validados"),
    path("canales-regiones", views.canales_regiones, name="canales-regiones"),
    path("spectrum-use-resp", views.spectrum_use_resp, name="spectrum-use-resp"), # para el maestro
    path("delete-channel-paws",views.delete_channel_paws, name="delete-channel-paws"), #para el maestro
    path("init-req", views.init_req, name="init-req"),# para el maestro
]
