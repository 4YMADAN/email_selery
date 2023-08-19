from django import forms

from .tasks import send_feedback_email_task


class ContactForm(forms.Form):
    from_email = forms.EmailField(label='Email', required=True)
    subject = forms.CharField(label='Тема', required=True)
    message = forms.CharField(label='Сообщение', widget=forms.Textarea, required=True)

    # def send_email(self):
    #     send_feedback_email_task.delay(
    #         self.cleaned_data["from_email"], self.cleaned_data["message"]
    #     )
    def send_email(self):
        send_feedback_email_task.apply_async(args=[
            self.cleaned_data["from_email"], self.cleaned_data["message"]
        ]
        )







        # sleep(20)
        #
        # send_mail(f"\t{self.cleaned_data['message']}\n\n Спасибо",  # f'{self.subject} от {self.from_email}'
        #           self.message,
        #           '4yma_dan@mail.ru'
        #           [self.cleaned_data['4ymadan@mail.ru']],
        #           fail_silently=False,
        #           )
