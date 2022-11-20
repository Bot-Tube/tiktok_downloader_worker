import os
from pathlib import Path
from dotenv import load_dotenv


ENV_PATH = Path(".") / "tiktok_downloader.env"
load_dotenv(dotenv_path=ENV_PATH)

def get_configuration():
    configuration = {
    "queue_name" : os.getenv("QUEUE_NAME"),
    "celery_config" : {
        "broker_url": os.getenv("BROKER_URL"),
        "broker_pool_limit": 1,
        "worker_prefetch_multiplier": 1,
        "worker_concurrency": 1,
        "worker_max_tasks_per_child": 1,
        "broker_connection_timeout": 120
    }}
    return configuration

def get_backend_api_url() -> str:
    return os.getenv("BACKEND_API")
