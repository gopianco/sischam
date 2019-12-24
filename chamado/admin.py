from django.contrib import admin
from chamado.models import Chamado, Cliente, Analista, Equipamento

admin.site.register(Chamado)
admin.site.register(Cliente)
admin.site.register(Analista)
admin.site.register(Equipamento)