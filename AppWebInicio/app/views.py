from django.shortcuts import render, HttpResponse

# Create your views here.
def saludo(request):
    return HttpResponse("Hola a todos desde PYTHON")

def index(request):
   documento='''
    <html>
    <body>

        <h1> Mi primera página con DJANGO... </h1>
    </body>

    </html>
    '''
   return HttpResponse(documento)