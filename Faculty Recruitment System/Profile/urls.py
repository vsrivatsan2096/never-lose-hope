from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^create$', views.create),
        url(r'^save$', views.save),
        url(r'^display$', views.display),
        url(r'^edit$', views.edit)
        ]

