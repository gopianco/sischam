# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User


class Equipamento(models.Model):
    id_equipamento = models.AutoField(primary_key=True)
    descricao = models.TextField(max_length=200, blank=False, null=False)
    local = models.TextField(max_length= 100)

    def __str__(self):
        return self.descricao

class Cliente(User):
    id_cliente = models.AutoField(primary_key=True)
    endereco = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class Analista(User):
    id_analista = models.AutoField(primary_key=True)
    class Meta:
        verbose_name = 'Analista'
        verbose_name_plural = 'Analistas'


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

    titulo_chamado = models.CharField(max_length=100, blank=False, null=False)
    id_chamado = models.AutoField(primary_key=True)
    tipo_chamado = models.CharField(max_length=20,choices=TIPO_DE_CHAMADO, default='Incidente')
    status= models.CharField(max_length=20, choices=STATUS_DE_CHAMADO, default='Aberto')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    analista = models.ForeignKey(Analista, on_delete=models.CASCADE, blank=True, null=True)
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    descricao = models.TextField()
    solucao = models.TextField(blank=True, null=True)
    #chat = models.ForeignKey()
    data_abertura = models.DateField(default=timezone.now)
    data_alteracao = models.DateField(default=timezone.now)
    

    def abrir_chamado(self):
        self.status = "ABERTO"
        self.data_abertura = timezone.now()
        self.save()
    
    def alterar_chamado(self):
        self.data_alteracao = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo_chamado

