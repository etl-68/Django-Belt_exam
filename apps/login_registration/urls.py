from django.conf.urls import url
from . import views

app_name="login_registration"

urlpatterns = [
    url(r'^$', views.start, name='start'),
    url(r'^actions', views.actions, name='actions'),
]
