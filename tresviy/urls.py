from django.conf.urls import url, include
from django.conf import settings


urlpatterns = [
    url(r'', include ('main.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
