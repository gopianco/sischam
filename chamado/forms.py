from django import forms
from .models import Chamado

class ChamadoForm(forms.ModelForm):

    titulo_chamado = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Dê um título para o seu problema...' 
        }
    ))
    CHOICES = Chamado.TIPO_DE_CHAMADO
    tipo_chamado = forms.ChoiceField(widget=forms.RadioSelect(
        attrs={
            'class': 'fom-control'
        }
    ), choices=CHOICES)

    STATUS = Chamado.STATUS_DE_CHAMADO
    status = forms.ChoiceField(widget=forms.Select(
        attrs={
            'class': 'form-control'
        }), choices=STATUS)

    descricao = forms.CharField(widget=forms.Textarea(
        attrs={
            'class':'form-control',
            'placeholder': 'Descreva seu chamado...'
        }
    ))

    class Meta:
        model = Chamado
        fields = ('titulo_chamado','tipo_chamado', 'status', 'equipamento', 'descricao' ) 

