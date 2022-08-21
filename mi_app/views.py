from django.shortcuts import render
from django.http import HttpResponse # hace que me devulva la info a la pag

from datetime import datetime

def saludo (request) :
    fecha_hora_ahora = datetime.now()
    return HttpResponse (f"Hola soy Ezequiel {fecha_hora_ahora}")



