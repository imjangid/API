from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include


urlpatterns = [
    url(r"^$", include("home.urls")),
    path('admin/', admin.site.urls),
    url(r'^ocr/', include("ocr.urls")),
    url(r'^anagram/', include("anagram.urls")),
]
