from celery import Celery
from kombu import Queue
from config import get_configuration

configuration = get_configuration()

celery = Celery("tasks", broker=configuration["celery_config"]["broker_url"])
celery.conf.update(**configuration["celery_config"])
celery.conf.task_queues = (Queue(configuration["queue_name"],
                                 routing_key="tasks." + configuration["queue_name"],
                                    **{"x-queue-mode": "lazy",
                                       "queue_arguments": {"x-queue-mode": "lazy"}}))

from tasks import tiktok_downloader_task
