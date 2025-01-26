import os
from celery import Celery
from celery.schedules import crontab

# Связываем настройки Django с настройками Celery через переменную окружения
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practice_project.settings')

# Создаем экземпляр приложения Celery
app = Celery('practice_project')
# Устанавливаем для экземпляра приложения Celery файл конфигурации.
# Указываем пространство имен, чтобы Celery сам находил все необходимые
# настройки в общем конфигурационном файле settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# Указываем Celery искать задания в файлах tasks.py каждого приложения проекта
app.autodiscover_tasks()
app.conf.broker_connection_retry_on_startup = False

app.conf.beat_schedule = {
    'print_every_5_seconds': {
        'task': 'celery_app.tasks.printer',
        'schedule': crontab(),
        'args': (5,),
    },
}
