# from config.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL

from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from .forms import ContactForm


class FeedbackFormView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = "success/"

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class SuccessView(TemplateView):
    template_name = "success.html"

# def contact_view(request):
#
#     if request.method == 'GET':         # если метод GET, вернем форму
#         form = ContactForm()
#     elif request.method == 'POST':      # если метод POST, проверим форму и отправим письмо
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.cleaned_data['subject']
#             from_email = form.cleaned_data['from_email']
#             message = form.cleaned_data['message']
#             try:
#                 form.send_email()
#                 # return super().form_valid(form)
#
#
#                 # send_mail(f'{subject} от {from_email}', message,
#                 #           from_email,
#                 #           ['4yma_dan@mail.ru'])
#             except BadHeaderError:                                  # исключение для перехвата
#                 return HttpResponse('Ошибка в теме письма.')
#             return redirect('success')
#     else:
#         return HttpResponse('Неверный запрос.')
#     return render(request, "contact.html", {'form': form})
#
# def success_view(request):
#     return HttpResponse('Приняли! Спасибо за вашу заявку.')
