from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from .views import *


urlpatterns = [
    url(r'^$', homepage),
]
