from django.urls import path
from . import views

urlpatterns = [
    path('alunos/cadastro/', views.cadastrar_aluno, name='cadastrar_aluno'),
]
