from django.conf.urls import url

from . import views

app_name = 'thread'

urlpatterns = [

	url(r'^$', views.index, name = 'index'),
	url(r'^(?P<thread_id>[0-9]+)/$', views.thread, name='thread')

]