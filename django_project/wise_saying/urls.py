from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^home$', views.home, name='home'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^me/$', views.my_post, name='my_post'),
]
