from django.urls import path
from app import views

# las rutas de la funciones 

urlpatterns = [
    path('saludo/',views.saludo,name='saludo'),
    path('index/',views.index,name='index'),
]