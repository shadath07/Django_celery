from django.core.mail import send_mail


def send_mail_without_celery():
    send_mail('Celery Worked Correctly','Celery is cool',
              'kingshad715@gmail.com', ['mohammedshadhath7@gmail.com'],
              fail_silently= False)
    return None