import redis
from django.http import HttpResponse
from django.views import View


class RedisView(View):
    def get(self, request, *args, **kwargs):
        red = redis.Redis(
            host='redis-11772.c8.us-east-1-2.ec2.redns.redis-cloud.com',
            port=11772,
            password='OXcSley25DmRO89VHwAqLL5OAkwehT1X'
        )
        return HttpResponse('Hello, World!')