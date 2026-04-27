# Create your views here.

from django.shortcuts import render
from .models import Escada

def lista_escadas(request):
    escadas = Escada.objects.all()
    return render(request, 'manutencao_app/lista_escadas.html', {'escadas': escadas})