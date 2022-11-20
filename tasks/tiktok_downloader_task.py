import random
from app import celery
from tiktok_downloader_worker import tiktok_downloader_worker


@celery.task(name="tasks.tiktok_downloader_task", bind=True, default_retry_delay=30 * 60,
             max_retries=3, time_limit=5.400)
def tiktok_downloader_task(self, **kwargs) -> None:
    """
    Celery worker receives tasks and executes command which sent in message.
    Sample of command_to_execute:
    'TiktokDownloader(**kwargs).execute_downloader()'
    Kwargs includes --> ??

    Parameters:
        self: Celery task object
        command_to_execute: ???
        kwargs: ???
    Returns:
        None
    """
    try:
        # TODO Change this structure. Structure down below is more safe.
        """
        :x: Problematic code:
            program = input('Enter code to be executed: ')
            exec(program)
        :heavy_check_mark: Correct code:
            programs = {'do_something': lambda: print("Do something")}
            program = input('Enter a program code to be used: ')
            if programs.get(program):
                programs[program]()
        """
        print("tiktok_downloader_task is running...")
        for item in kwargs:
            print(item)
    except Exception as general_exception:
        # TODO: More specific exceptions required.
        # Log an exception here.
        self.retry(exc=general_exception, countdown=int(random.uniform(1, 3)))
