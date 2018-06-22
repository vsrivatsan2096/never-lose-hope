from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^index/$', views.index),
        url(r'^academics/$', views.academics),
        url(r'^contact/$', views.contact),
        ]