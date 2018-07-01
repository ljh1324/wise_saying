from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.register, name='login'),
    url(r'^home$', views.register, name='home'),
]
