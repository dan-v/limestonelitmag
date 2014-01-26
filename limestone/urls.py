from django.conf.urls import patterns, url

from limestone import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^submit', views.submit, name='submit'),
	url(r'^about', views.about, name='about'),
	url(r'^archive', views.archives, name='archives'),
	url(r'^issues/(?P<number>([0-9]+))/$', views.issue, name='issue')
)
