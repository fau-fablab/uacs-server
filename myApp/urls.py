from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # asking for a specific cardid

    url(r'^users/([-\w\-]+)/$', views.detail, name='detail'),
    url(r'^devices/([-\w\-]+)/$', views.devices, name='devices'),
    url(r'^create/$', views.create, name='create'),
    url(r'newUser/$', views.newUser, name='newUser'),
    url(r'^strikeUser/$', views.strikeUser, name='strikeUser'),
]
