from django import forms


class ContactForm(forms.Form):
    author = forms.CharField(label='Автор сообщения', required=True)
    subject = forms.CharField(label='Тема сообщения', required=True)
    message = forms.CharField(label='Текст сообщения', widget=forms.Textarea, required=True)
