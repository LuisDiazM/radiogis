from django.urls import path 
from . import views
from . import apiviews

app_name = "nariz_electronica"
urlpatterns = [
    path("index", views.index, name="index-nariz"),
    path("lecturas", apiviews.LecturasAPI.as_view()),
    path("clasificar_datos", apiviews.DatosEvaluarAPI.as_view()),
    path("analisis", views.analisis_nariz, name="analisis_nariz"),
    path("entrenamiento", views.entrenamiento, name="entrenamiento"),
    path("seleccion_entrenamiento", views.recolectar_datos_entrenamiento, name="seleccion-entrenamiento"),
    path("toma_datos", views.toma_datos, name="toma-datos"),
    path("evaluacion_clasificadores", views.evaluacion_clasificadores, name="evaluacion-clasificadores"),
    path("clasificacion_maderas", views.clasificacion_maderas, name="clasificacion-maderas"),
    path("clasificacion_rocas", views.clasificacion_rocas, name="clasificacion-rocas"),
    path("clasificacion_triatominos", views.clasificacion_triatominos, name="clasificacion-triatominos"),


]
