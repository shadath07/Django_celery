from celery import shared_task
from time import sleep
from django.core.mail import send_mail

@shared_task
def sleepy(duariton):
    sleep(duariton)
    return None

@shared_task
def send_mail_task():
    send_mail('Celery Worked Correctly','Celery is cool',
              'kingshad715@gmail.com', ['mohammedshadhath7@gmail.com'],
              fail_silently= False)
    print("MAIL FROM CELERY")
    return None

