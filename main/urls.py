from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
	# main page
    url(r'^$', views.Main, name="mainview"),
]
