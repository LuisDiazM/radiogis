from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Variables

# Create your views here.
def index(request):
    respuesta = {}
    return render(request, "E3Tratos/index.html", respuesta)

@csrf_exempt
def datos_json(request):
    var = Variables.objects.last()
    respuesta = {"datos": [var.fecha, var.variables]}
    print(respuesta)
    return JsonResponse(respuesta)

def gui(request):
    return render(request, "E3Tratos/gui.html", {})


def docs(request):
    return render(request, "E3Tratos/docs.html", {})

def media(request):
    return render(request, "E3Tratos/media.html", {})

def contact(request):
	print("hola contacto")
	return render(request, "E3Tratos/contact.html", {})

@csrf_exempt
def datos_json_all(request):
    var = Variables.objects.all()
    datos = var.values("fecha", "variables")
    datos = list(map(lambda datos: [datos["fecha"], datos["variables"]], datos))
    respuesta = {"datos": datos}
    return JsonResponse(respuesta)