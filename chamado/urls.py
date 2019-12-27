from django.urls import path
from . import views

urlpatterns = [
    path('', views.chamados_list, name='chamados_list'),
    path('chamado/<int:pk>/', views.chamado_details, name='chamado_detail'),
    path('chamado/new/', views.chamado_new, name='chamado_new'),
    path('chamado/<int:pk>/edit/', views.chamado_edit, name='chamado_edit'),
]