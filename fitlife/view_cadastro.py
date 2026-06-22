from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno, Pagamento, Fatura, Modalidade, Turma


def cadastrar_aluno(request):
    if request.method == 'POST':
        cpf             = request.POST.get('cpf')
        nome_aluno      = request.POST.get('nome_aluno')
        data_nascimento = request.POST.get('data_nascimento')
        endereco_aluno  = request.POST.get('endereco_aluno')
        telefone_aluno  = request.POST.get('telefone_aluno')
        e_mail          = request.POST.get('e_mail')
        restricoes      = request.POST.get('restricoes')

        Aluno.objects.create(
            cpf             = cpf,
            nome_aluno      = nome_aluno,
            data_nascimento = data_nascimento,
            endereco_aluno  = endereco_aluno,
            telefone_aluno  = telefone_aluno,
            e_mail          = e_mail,
            restricoes      = restricoes
        )

        return redirect('listar_alunos')

    return render(request, 'fitlife/cadastrar_aluno.html')
