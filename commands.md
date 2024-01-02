celery -A dcelery.celery worker -l info
celery -A dcelery.celery flower

celery -A dcelery beat -l INFO --scheduler django_celery_beat schedulers:DatabaseScheduler