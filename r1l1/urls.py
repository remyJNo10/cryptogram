from django.conf.urls import url

from . import views

app_name = 'r1l1'

urlpatterns = [
    url(r'^', views.index, name='index'),
    url(r'^gotonextlevel', views.verify, name='verify'),
]