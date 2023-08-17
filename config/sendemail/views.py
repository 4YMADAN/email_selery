# from config.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm


def contact_view(request):

    if request.method == 'GET':         # если метод GET, вернем форму
        form = ContactForm()
    elif request.method == 'POST':      # если метод POST, проверим форму и отправим письмо
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(f'{subject} от {from_email}', message,        # отправка сообщений
                          from_email,                                    # адрес отправителя
                          ['4yma_dan@mail.ru'])                         # адрес получателя
            except BadHeaderError:                                  # исключение для перехвата
                return HttpResponse('Ошибка в теме письма.')
            return redirect('success')
    else:
        return HttpResponse('Неверный запрос.')
    return render(request, "contact.html", {'form': form})

def success_view(request):
    return HttpResponse('Приняли! Спасибо за вашу заявку.')
