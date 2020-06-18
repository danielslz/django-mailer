from celery import shared_task
from celery.utils.log import get_logger
from django.core import management


@shared_task
def send_mail():
    logger = get_logger(send_mail.__name__)
    logger.info("Sending mails")
    management.call_command("send_mail", verbosity=0)


@shared_task
def retry_deferred():
    logger = get_logger(retry_deferred.__name__)
    logger.info("Retrying sending deferred mails")
    management.call_command("retry_deferred", verbosity=0)


@shared_task
def purge_mail_log(days):
    logger = get_logger(purge_mail_log.__name__)
    logger.info("Purging mails logs")
    management.call_command("purge_mail_log", days, verbosity=0)
