import random
from app import celery, configuration
from tiktok_downloader import tiktok_downloader_worker


@celery.task(name="tasks." + configuration["queue_name"], bind=True, default_retry_delay=30 * 60,
             max_retries=3, time_limit=5.400)
def tiktok_downloader_task(self, command_to_execute, **kwargs) -> None:
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
        exec(command_to_execute)
    except Exception as general_exception:
        # TODO: More specific exceptions required.
        # Log an exception here.
        self.retry(exc=general_exception, countdown=int(random.uniform(1, 3)))
