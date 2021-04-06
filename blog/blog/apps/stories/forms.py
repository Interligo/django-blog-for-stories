from django import forms
from django.utils.safestring import mark_safe


class LeaveCommentForm(forms.Form):
    author = forms.CharField(label=mark_safe('<strong>Автор комментария</strong>'), widget=forms.TextInput(
        attrs={
            'type': 'text',
            'class': 'form-control',
            'style': 'width: 400px; height: 35px;'
        }))
    text = forms.CharField(label=mark_safe('<strong>Текст комментария</strong>'), widget=forms.Textarea(
        attrs={
            'type': 'text',
            'class': 'form-control',
            'style': 'width: 400px; height: 100px;'
        }))
