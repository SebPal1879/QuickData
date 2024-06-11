from django import forms

from .models import archivo

class archivo_formulario(forms.ModelForm):
    nombre = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control form-control-lg','required':''}))
    subir_archivo = forms.FileField(required=True,widget=forms.FileInput(attrs={'class': 'form-control form-control-lg','type':'file','id':'formFile','required':''}))
    class Meta:
        model = archivo
        fields = {'nombre', 'subir_archivo'}
        

    
    