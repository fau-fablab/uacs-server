from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	# asking for a specific cardid

	url(r'^users/([-\w\-]+)/$', views.detail, name='detail'),
	url(r'^devices/([-\w\-]+)/$', views.devices, name='devices'),
	url(r'^create/([-\w\-]+)/$', views.create, name='create'),
]
