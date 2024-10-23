from django import forms
from .models import Lesson

class LessonForm(forms.ModelForm):
    date = forms.DateField(
        label='Дата',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        input_formats=['%Y-%m-%d', '%d.%m.%Y'],
    )
    time = forms.TimeField(
        label='Время',
        widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        input_formats=['%H:%M', '%H:%M:%S'],
    )

    class Meta:
        model = Lesson
        fields = ['name', 'date', 'time', 'classroom', 'group', 'day_of_week']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'classroom': forms.TextInput(attrs={'class': 'form-control'}),
            'group': forms.Select(attrs={'class': 'form-select'}),
            'day_of_week': forms.Select(attrs={'class': 'form-select'}),
        }