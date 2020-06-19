from celery import shared_task, current_app
from celery.schedules import crontab
from celery.utils.log import get_logger
from django.conf import settings
from django.core import management


# Get taks schedules
MAILER_DAYS_PURGE_MAIL_LOG = int(getattr(settings, 'MAILER_DAYS_PURGE_MAIL_LOG', 7))
MAILER_MINUTS_TO_RETRY_DEFERRED = int(getattr(settings, 'MAILER_MINUTS_TO_RETRY_DEFERRED', 30))
MAILER_MINUTS_TO_SEND_MAIL = int(getattr(settings, 'MAILER_MINUTS_TO_SEND_MAIL', 5))


current_app.conf.beat_schedule = {
    # Executes every minute
    'send_mail': {
        'task': 'mailer.tasks.send_mail',
        'schedule': crontab(minute='*/{}'.format(MAILER_MINUTS_TO_SEND_MAIL)),
    },
    # Execute every 20 minutes
    'retry_deferred': {
        'task': 'mailer.tasks.retry_deferred',
        'schedule': crontab(minute='*/{}'.format(MAILER_MINUTS_TO_RETRY_DEFERRED)),
    },
    # Execute daily at midnight
    'purge_mail_log': {
        'task': 'mailer.tasks.purge_mail_log',
        'schedule': crontab(minute=0, hour=0),
        'kwargs': {'days': MAILER_DAYS_PURGE_MAIL_LOG},
    },
}


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
