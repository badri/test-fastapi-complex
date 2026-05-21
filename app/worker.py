import os
from celery import Celery

REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379/0")
celery_app = Celery("worker", broker=REDIS_URL, backend=REDIS_URL)

@celery_app.task
def process_task(payload: str) -> str:
    return f"processed: {payload}"
