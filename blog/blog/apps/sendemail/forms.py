from django import forms
from django.utils.safestring import mark_safe


class ContactForm(forms.Form):
    author = forms.CharField(label=mark_safe('<strong>Автор сообщения</strong>'), widget=forms.TextInput(
        attrs={
            'type': 'text',
            'class': 'form-control'
        }))
    subject = forms.CharField(label=mark_safe('<strong>Тема сообщения</strong>'), widget=forms.TextInput(
        attrs={
            'type': 'text',
            'class': 'form-control'
        }))
    message = forms.CharField(label=mark_safe('<strong>Текст сообщения</strong>'), widget=forms.Textarea(
        attrs={
            'type': 'text',
            'class': 'form-control'
        }))
    email = forms.EmailField(label='Почта для обратной связи', required=False, widget=forms.HiddenInput(
        attrs={
            'type': 'email',
            'class': 'form-control'
        }))
