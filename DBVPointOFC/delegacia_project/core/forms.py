from django import forms
from .models import Policial, Ocorrencia, Vitima, Suspeito, Evidencia

class PolicialForm(forms.ModelForm):
    class Meta:
        model = Policial
        fields = '__all__'

class OcorrenciaForm(forms.ModelForm):
    class Meta:
        model = Ocorrencia
        fields = '__all__'

class VitimaForm(forms.ModelForm):
    class Meta:
        model = Vitima
        fields = '__all__'

class SuspeitoForm(forms.ModelForm):
    class Meta:
        model = Suspeito
        fields = '__all__'

class EvidenciaForm(forms.ModelForm):
    class Meta:
        model = Evidencia
        fields = '__all__'
