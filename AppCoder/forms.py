from django import forms

class EquipoFormulario(forms.Form):
    
    nombre = forms.CharField()
    provincia = forms.CharField()

class JugadorFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    peso = forms.FloatField()
    altura = forms.FloatField()
    equipo = forms.CharField()

class EntrenadorFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    equipo = forms.CharField()        

class ArbitroFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    nacionalidad = forms.CharField()

