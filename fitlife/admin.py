from django.contrib import admin
from .models import Aluno, Professor, Plano, ContratoPlan, Pagamento, Fatura, Modalidade, Turma, Inscricao, Unidade
# Register your models here.
admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Plano)
admin.site.register(ContratoPlan)
admin.site.register(Pagamento)
admin.site.register(Fatura)
admin.site.register(Modalidade)
admin.site.register(Turma)
admin.site.register(Inscricao)
admin.site.register(Unidade)
