from django.shortcuts import render
from .models import Chamado

def chamados_list(request):
    chamados = Chamado.objects.all().order_by('data_abertura')
    return render(request, 'chamado/chamados_list.html', {'chamados': chamados})
