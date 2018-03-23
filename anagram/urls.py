from django.contrib import admin
from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r"word=(?P<word>[\w]+)", find),
    url(r"", error),
]
