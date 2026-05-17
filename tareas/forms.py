from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):

    class Meta:
        model = Tarea

        fields = [
            'titulo',
            'descripcion',
            'estado',
            'prioridad',
            'fecha_limite'
        ]

        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Título de tarea...'
            }),

            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Añada detalles sobre esta tarea...',
                'rows': 10
            }),

            'estado': forms.Select(attrs={
                'class': 'form-select form-select-lg'
            }),

            'prioridad': forms.Select(attrs={
                'class': 'form-select form-select-lg'
            }),

            'fecha_limite': forms.DateInput(attrs={
                'class': 'form-control form-control-lg',
                'type': 'date'
            }),
        }