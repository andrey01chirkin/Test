from django.urls import path
from redis_app.views import RedisView

urlpatterns = [
    path('', RedisView.as_view(), name='redis'),
]