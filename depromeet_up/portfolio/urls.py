from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^write/$', views.write ,name='write'),
    url(r'^write/post$', views.post, name='entire_view'),
    ]