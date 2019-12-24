from django.urls import path
from . import views

urlpatterns = [
    path('', views.chamados_list, name='chamados_list'),
]