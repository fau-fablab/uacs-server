from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	# asking for a specific cardid
	url(r'^(?P<wantedcardid>[-\w\-]+)/$', views.detail, name='detail'),
]
