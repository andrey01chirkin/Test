import os
from datetime import timedelta, datetime

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practice_project.settings')  # Замените myproject на имя вашего проекта
django.setup()

from practice_app.models import *



