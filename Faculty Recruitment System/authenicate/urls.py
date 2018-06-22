from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^signin/$', views.signin),
        url(r'^validate/$', views.validate),
        url(r'^signup/$', views.signup),
        url(r'^create/$',views.create),
        url(r'^invalid/$', views.invalid),
        url(r'^logout/$', views.logout),
        ]