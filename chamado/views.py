from django.shortcuts import render

def chamados_list(request):
    return render(request, 'chamado/chamados_list.html', {})
