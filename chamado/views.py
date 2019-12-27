from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from django.shortcuts import redirect
from django.shortcuts import render
from .models import Chamado
from .forms import ChamadoForm


def chamados_list(request):
    chamados = Chamado.objects.filter(cliente=1).order_by('status')
    return render(request, 'chamado/chamados_list.html', {'chamados': chamados})

def chamado_details(request, pk):
    chamado = get_object_or_404(Chamado, pk=pk)
    return render(request, 'chamado/chamado_detail.html', {'chamado': chamado})

def chamado_new(request):
    if request.method == 'POST':
        form = ChamadoForm(request.POST)
        if form.is_valid:
            chamado = form.save(commit=False)
            chamado.data_abertura = timezone.now()
            chamado.data_alteracao = timezone.now()
            chamado.cliente_id = 1
            chamado.save()
            return redirect('chamado_detail', pk=chamado.pk)

    else:
        form = ChamadoForm()
    return render(request, 'chamado/chamado_edit.html', {'form': form})

def chamado_edit(request, pk):
    chamado = get_object_or_404(Chamado, pk=pk)
    if request.method == 'POST':
        form = ChamadoForm(request.POST, instance=chamado)
        if form.is_valid:
            chamado = form.save(commit=False)
            chamado.data_abertura = timezone.now()
            chamado.data_alteracao = timezone.now()
            chamado.cliente_id = 1
            chamado.save()
            return redirect('chamado_detail', pk=chamado.pk)
    else:
        form= ChamadoForm(instance=chamado)
    return render(request, 'chamado/chamado_edit.html', {'form': form})


