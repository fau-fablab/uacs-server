from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	# asking for a specific fauid
	url(r'^(?P<wantedfauid>[0-99999]+)/$', views.detail, name='detail'),
]
