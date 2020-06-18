from celery import shared_task, Celery
from celery.utils.log import get_logger

from django.core import management

# app = Celery('mailer')
#
# app.config_from_object('django.conf:settings', namespace='CELERY')


@shared_task
def send_mail():
    logger = get_logger(send_mail.__name__)
    logger.info("Sending mails")
    management.call_command("send_mail", verbosity=0)


@shared_task
def retry_deferred():
    logger = get_logger(send_mail.__name__)
    logger.info("Retrying sending deferred mails")
    management.call_command("retry_deferred", verbosity=0)


@shared_task
def purge_mail_log(days):
    logger = get_logger(send_mail.__name__)
    logger.info("Retrying sending deferred mails")
    management.call_command("purge_mail_log", days=days, verbosity=0)
