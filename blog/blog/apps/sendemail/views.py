from typing import Optional

from django.core.mail import send_mail
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

from django.conf import settings
from sendemail.forms import ContactForm


SUCCESS_MESSAGE = 'Сообщение отправлено!'
ERROR_MESSAGE = 'Ошибка отправки сообщения.'


def _send_email(author: str, subject: str, message: str, email: Optional[str] = None) -> bool:
    """For sending email and returning boolean value to print message on site."""
    email_to_get_answer = email if email else 'не указана'
    return send_mail(
        subject,
        f'Сообщение:\n{message} \nПочта для обратной связи: {email_to_get_answer} \nАвтор сообщения: {author}',
        settings.EMAIL_HOST_USER,
        (settings.RECIPIENT_MAIL,),
        fail_silently=False
    )


def contact_view(request):
    """For contact with site author."""
    if request.method == 'GET':
        form = ContactForm()
        return render(request, 'sendemail/email.html', {'form': form})

    form = ContactForm(request.POST)
    if form.is_valid():
        is_mail_send = _send_email(
            author=form.cleaned_data['author'],
            subject=form.cleaned_data['subject'],
            message=form.cleaned_data['message'],
            email=form.cleaned_data['email']
        )

        if not is_mail_send:
            messages.error(request, ERROR_MESSAGE)
            return render(request, 'sendemail/email.html', {'form': form})

    messages.success(request, SUCCESS_MESSAGE)
    return HttpResponseRedirect(reverse('sendemail:contact'))
