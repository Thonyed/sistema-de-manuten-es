from django.urls import path
from .views import lista_escadas
from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('escada/', views.lista_escadas, name='lista_escadas'),
#     path('criar/', views.criar_escada, name='criar_escada'),
#     path('escada/<int:id>/', views.detalhe_escada, name='detalhe_escada'),
#     path('escada/<int:id>/concluir/', views.concluir_escada, name = 'concluir_escada'),
#     path('api/escadas/', views.lista_escadas),
# ]

urlpatterns = [
    path('', views.home, name='home'),
    # HTML
    path('escada/', views.lista_escadas, name='lista_escadas'),

    # API
    path('api/escadas/', views.api_lista_escadas),

    path('criar/', views.criar_escada, name='criar_escada'),
    path('escada/<int:id>/', views.detalhe_escada, name='detalhe_escada'),
    path('escada/<int:id>/concluir/', views.concluir_escada, name='concluir_escada'),
    path('status/', views.status_escadas, name='status_escadas'),
    path('status/<int:id>/', views.atualizar_status, name='atualizar_status'),
]