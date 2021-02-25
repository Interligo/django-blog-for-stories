from django.core.mail import send_mail
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

from django.conf import settings
from .forms import ContactForm


def contact_view(request):
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            if not form.cleaned_data['email']:
                email = 'не указана.'
            else:
                email = form.cleaned_data['email']

            is_mail_send = send_mail(subject, f'Сообщение:\n{message} \nПочта для обратной связи: {email} '
                                              f'\nАвтор сообщения: {author}',
                                     settings.EMAIL_HOST_USER, (settings.RECIPIENT_MAIL,), fail_silently=False)
            if is_mail_send:
                messages.success(request, 'Сообщение отправлено!')
                return HttpResponseRedirect(reverse('sendemail:contact'))
            else:
                messages.error(request, 'Ошибка отправки сообщения.')

    return render(request, 'sendemail/email.html', {'form': form})
