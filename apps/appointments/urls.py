from django.conf.urls import url
from . import views

app_name="appointments"

urlpatterns = [
    url(r'^$', views.start, name='start'),
    url(r'^new$', views.new, name='new'),
    url(r'^edit/(?P<id>[0-9]+$)', views.edit, name='edit'),
    url(r'^delete/(?P<id>[0-9]+$)', views.delete, name='delete'),
    url(r'^change/(?P<id>[0-9]+$)', views.change, name='change'),
]
