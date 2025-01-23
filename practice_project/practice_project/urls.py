from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('protect_app.urls')),
    path('sign/', include('sign_app.urls')),
    path('accounts/', include('allauth.urls')),
    path('email/', include('appointment_app.urls')),
]
