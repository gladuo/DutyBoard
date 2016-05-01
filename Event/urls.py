from django.conf.urls import patterns, url
from Event import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]
