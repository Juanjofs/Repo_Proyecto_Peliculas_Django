from django import forms
from apps.videoclub.models import *

class PeliculaForm(forms.ModelForm):

    class Meta:
        model = Pelicula

        fields = [
            'titulo',
            'url_trailer',
            'fecha',
            'nota',
            'sinopsis',
            'genero',
            'director',
            'actores',
            'caratula',
            'imagen_promocional',
        ]

        labels = {
            'titulo':'Título',
            'url_trailer':'URL Trailer',
            'fecha':'Fecha',
            'nota':'Nota',
            'sinopsis':'Sinopsis',
            'genero':'Género',
            'director':'Director',
            'actores':'Actores',
            'caratula':'Carátula',
            'imagen_promocional':'Imágen promocional',
        }

        notas_posibles = (
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5)
        )

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'url_trailer': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.SelectDateWidget(years=range(1900,2025)),
            'nota': forms.Select(attrs={'class': 'form-control'}, choices=notas_posibles), 
            'sinopsis': forms.Textarea(attrs={'class': 'form-control'}),
            'genero': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'director': forms.Select(attrs={'class': 'form-control'}),
            'actores': forms.SelectMultiple(attrs={'class': 'form-control'}),
            # 'caratula': forms.ImageField(),
            # 'imagen_promocional': forms.ImageField(),
        }
