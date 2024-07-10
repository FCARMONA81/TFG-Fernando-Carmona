from django import forms
from .models import Objetivo, Indicador, AGC, UGC, AcuerdoIndicadores

class ObjetivoForm(forms.ModelForm):
    class Meta:
        model = Objetivo
        fields = '__all__'

class IndicadorForm(forms.ModelForm):
    class Meta:
        model = Indicador
        fields = '__all__'

class AGCForm(forms.ModelForm):
    class Meta:
        model = AGC
        fields = '__all__'

class UGCForm(forms.ModelForm):
    class Meta:
        model = UGC
        fields = '__all__'

class AcuerdoIndicadoresForm(forms.ModelForm):
    class Meta:
        model = AcuerdoIndicadores
        fields = '__all__'


class UploadExcelForm(forms.Form):
    excel_file = forms.FileField()