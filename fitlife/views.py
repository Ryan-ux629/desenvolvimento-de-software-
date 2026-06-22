from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno, Pagamento, Fatura, Modalidade, Turma


def listar_alunos(request):
    alunos = Aluno.objects.all()

    busca  = request.GET.get('busca')
    ordem  = request.GET.get('ordem')

    if busca:
        alunos = alunos.filter(nome_aluno__icontains=busca)

    if ordem == 'nome_za':
        alunos = alunos.order_by('-nome_aluno')
    elif ordem == 'nascimento':
        alunos = alunos.order_by('data_nascimento')
    else:
        alunos = alunos.order_by('nome_aluno')

    return render(
        request,
        'fitlife/listar_alunos.html',
        {
            'alunos': alunos,
            'busca': busca,
            'ordem': ordem,
        }
    )
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

def editar_aluno(request, cpf):
    aluno = get_object_or_404(Aluno, cpf=cpf)

    if request.method == 'POST':
        aluno.nome_aluno      = request.POST.get('nome_aluno')
        aluno.data_nascimento = request.POST.get('data_nascimento')
        aluno.endereco_aluno  = request.POST.get('endereco_aluno')
        aluno.telefone_aluno  = request.POST.get('telefone_aluno')
        aluno.e_mail          = request.POST.get('e_mail')
        aluno.restricoes      = request.POST.get('restricoes')
        aluno.save()

        return redirect('listar_alunos')

    return render(
        request,
        'fitlife/editar_aluno.html',
        {'aluno': aluno}
    )
def detalhe_aluno(request, cpf):
    aluno = get_object_or_404(Aluno, cpf=cpf)

    return render(
        request,
        'fitlife/detalhe_aluno.html',
        {'aluno': aluno}
    )
def excluir_aluno(request, cpf):
    aluno = get_object_or_404(Aluno, cpf=cpf)

    if request.method == 'POST':
        aluno.delete()
        return redirect('listar_alunos')

    return render(
        request,
        'fitlife/confirmar_exclusao.html',
        {'aluno': aluno}
    )
