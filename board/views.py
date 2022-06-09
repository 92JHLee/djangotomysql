from django.http import HttpResponse
from django.shortcuts import render
from .models import Booktbl  # Booktbl 모델 불러오기
from django.db.models import Q
from django.views.generic import DetailView


# Create your views here.
def index(request):
    return HttpResponse('Welcome! This is TRPG WORLD!')


def board_list(request):
    posts = Booktbl.objects.all()
    return render(request,
                  'index.html',
                  {"posts": posts}
                  )


def article(request, id):
    post = Booktbl.objects.get(id=id)
    return render(request,
                  'detail.html',
                  {"post": post}
                  )


def search(request):
    if 'kw' in request.GET:
        query = request.GET.get('kw')
        posts = Booktbl.objects.all().filter(
            Q(bookname__icontains=query) |
            Q(title__icontains=query) |
            Q(author__icontains=query)
        )
        return render(request,
                      'search.html',
                      {'query': query, 'posts': posts}
                      )

# render : API 리턴값으로 템플릿지정가능
# render(request, template_name, Context=None}
# context : 위의 인자와 함께 html에 리턴하고 시은 dictionary 지정
# ex: copntext={'cities':all_cities} > html에서 {{key}}로 접근가능
#
# def detail(request,board_id):
#     board = Booktbl.objects.get(id=board_id)
#     return render(request,
#                   'board/detail.html',
#                   {'board':board}
#                   )
