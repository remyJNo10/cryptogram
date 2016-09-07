from django.conf.urls import url

from . import views

app_name = 'login'

urlpatterns = [
    url(r'^$', views.ShowLogin, name='ShowLogin'),
    url(r'^loginaction/$', views.PerformLoginAction, name="PerformLoginAction"),
]