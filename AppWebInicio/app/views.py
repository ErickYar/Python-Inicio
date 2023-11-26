from django.shortcuts import render, HttpResponse

# Create your views here.
def saludo(request):
    return HttpResponse("Hola a todos desde PYTHON")
