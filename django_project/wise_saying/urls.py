from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),  # 메인
    url(r'^register$', views.register, name='register'), # 회원 가입
    url(r'^login$', views.login, name='login'), # 로그인
    url(r'^logout$', views.logout, name='logout'), # 로그아웃
    url(r'^home$', views.home, name='home'), # 로그인 후 홈
    url(r'^post$', views.post, name='post'), # 명언 보기
    url(r'^post/new/$', views.post_new, name='post_new'), # 명언 작성
    url(r'^post/me/$', views.post_me, name='my_post'), # 나의 명언 보기
    url(r'^like$', views.like, name='like'), # 좋아요
]
