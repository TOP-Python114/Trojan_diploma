from .models import Vacancy
from django.forms import ModelForm, TextInput, Textarea


class VacancyForm(ModelForm):
    class Meta:
        model = Vacancy
        fields = [
            'position',
            'salary',
            'work_schedule',
            'responsibilities',
            'requirements',
            'working_conditions'
        ]

        widgets = {
            "position": TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Название вакансии'
            }),
            "salary": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заработная плата'
            }),
            "work_schedule": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'График работы'
            }),
            "responsibilities": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Обязанности'
            }),
            "requirements": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Требования'
            }),
            "working_conditions": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Условия'
            })
        }