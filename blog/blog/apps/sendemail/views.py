from django.core.mail import send_mail
from django.core.mail import BadHeaderError
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
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
            try:
                is_mail_send = send_mail(f'{subject} от {author}', message,
                          settings.EMAIL_HOST_USER, settings.RECIPIENT_LIST, fail_silently=False)
                if is_mail_send:
                    messages.success(request, 'Сообщение отправлено!')
                    return redirect('main.index')
                else:
                    messages.errer(request, 'Ошибка отправки :(')
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return redirect('success')
    else:
        return HttpResponse('Неверный запрос.')
    return render(request, 'sendemail/email.html', {'form': form})
