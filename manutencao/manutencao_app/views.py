# Create your views here.
from .models import Escada
from .forms import EscadaForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EscadaSerializer 
from django.shortcuts import render, redirect, get_object_or_404


def lista_escadas(request):
    escadas = Escada.objects.all()
    return render(request, 'manutencao_app/lista_escadas.html', {'escadas': escadas})


@api_view(['GET'])
def api_lista_escadas(request):
    escadas = Escada.objects.all()
    serializer = EscadaSerializer(escadas, many=True)
    return Response(serializer.data)
    
def criar_escada(request):
    if request.method == 'POST':
        form = EscadaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_escadas')
    else:
        form = EscadaForm()

    return render(request, 'manutencao_app/criar_escada.html', {'form': form})

def detalhe_escada(request, id):
    escada = get_object_or_404(Escada, id=id)
    return render(request, 'manutencao_app/detalhe_escada.html', {'escada': escada})

def concluir_escada (request, id):
    escada = get_object_or_404(Escada, id=id)
    escada.status = 'concluida'
    escada.save()
    return redirect('detalhe_escada', escada.id)

def home(request):
    return render(request, 'manutencao_app/home.html')