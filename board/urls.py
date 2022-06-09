"""djangotomysql URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#http://127.0.0.1/ 메인페이지
#http://127.0.0.1/board 전체 목록보이기
#http://127.0.0.1/board/article/1 읽기
#http://127.0.0.1/board/create 생성
#http://127.0.0.1/board/search/1 검색결과값
# 수정은..미래의 내가..


from django.urls import path
from board import views
from board.views import search

urlpatterns = [
    path('', views.index,name='index'),
    path('board/', views.board_list,name='board_list'),
    path('board/article/<id>',views.article,name='article'),
    path('board/search/<id>',views.search,name='search'),


]