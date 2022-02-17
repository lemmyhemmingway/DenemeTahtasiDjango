import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DenemeTahtasi.settings')

app = Celery('DenemeTahtasi')

app.config_from_project('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
