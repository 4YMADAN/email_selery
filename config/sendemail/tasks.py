from time import sleep

from celery import shared_task
from django.core.mail import send_mail


@shared_task()                          # настройка задачи, которая обеспечивает возможность повторного использования
                                        # ваших приложений.
def send_feedback_email_task(email_address, message):

    sleep(20)
    send_mail(
        f"\t{message}\n\n Спасибо",
        '4yma_dan@mail.ru',
        [email_address],
        fail_silently=False,
    )