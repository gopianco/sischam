# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User


class Cliente(User):
    endereco = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

class Analista(User):
    is_staff = True
    class Meta:
        verbose_name = 'Analista'
        verbose_name_plural = 'Analistas'


class Equipamento(models.Model):
    id_equipamento = models.AutoField(primary_key=True)
    descricao = models.TextField(max_length=200, blank=False, null=False)
    local = models.TextField(max_length= 100)


class Chamado(models.Model):

    TIPO_DE_CHAMADO = [
        ("INCIDENTE", 'Incidente'),
        ("REQUISICAO", 'Requsição'),
    ]

    STATUS_DE_CHAMADO = [
        ("ABERTO" ,'Aberto'),
        ("EM_ANDAMENTO", 'Em andamento'),
        ("AGUARDANDO", 'Aguardando'),
        ("CONCLUIDO", 'Concluido'),
    ]

    id_chamado = models.AutoField(primary_key=True)
    tipo_chamado = models.CharField(max_length=20,choices=TIPO_DE_CHAMADO, default='Incidente')
    status= models.CharField(max_length=20, choices=STATUS_DE_CHAMADO, default='Aberto')
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    analista = models.OneToOneField(Analista, on_delete=models.CASCADE)
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    descricao = models.TextField()
    solucao = models.TextField()
    #chat = models.ForeignKey()
    data_abertura = models.DateField(auto_now=True)

