from django.shortcuts import render
from .models import Chamado

def chamados_list(request):
    chamados = Chamado.objects.filter(cliente=1).order_by('status')
    return render(request, 'chamado/chamados_list.html', {'chamados': chamados})
