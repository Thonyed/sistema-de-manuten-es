from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_escadas, name='lista_escadas'),
    path('criar/', views.criar_escada, name='criar_escada'),
    path('escada/<int:id>/', views.detalhe_escada, name='detalhe_escada'),
    path('escada/<int:id>/concluir', views.concluir_escada, name = 'concluir_escada'),
]