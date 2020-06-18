from celery import shared_task, Celery
from celery.utils.log import get_logger

from django.core import management

app = Celery('django-mailer')

app.config_from_object('django.conf:settings', namespace='CELERY')


@shared_task
def send_mail():
    logger = get_logger(send_mail.__name__)
    logger.info("Sending mails")
    print("Sending mails")
    # management.call_command("send_mail", verbosity=0)
