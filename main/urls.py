from django.conf.urls import url
from main.views import *


urlpatterns = [
	url(r'^$', ComingView.as_view(), name="coming"),
]
