from django import forms
from .models import Application


class ApplicationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Почта'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Номер телефона'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Комментарий'}))

    class Meta:
        model = Application
        fields = '__all__'
