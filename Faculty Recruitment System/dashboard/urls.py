from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^dashboard/$', views.dashboard),
        url(r'^cse/$', views.cse),
        url(r'^civil/$', views.civil),
        url(r'^eee/$', views.eee),
        url(r'^ece/$', views.ece),
        url(r'^mech/$', views.mech),
        url(r'^status/$', views.status),
        url(r'^support/$', views.support),
        url(r'^office/$', views.office),
        url(r'^apply/$', views.apply),
]
