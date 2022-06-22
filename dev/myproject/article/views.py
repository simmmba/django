from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Article


def article_list(request):
    qs = Article.objects.all()
    # 'q' key값 갖는 dictionary value 가져오기, 없을때 ''
    keyword = request.GET.get('q', '')

    # 검색어 검색하기
    if keyword:
        qs = Article.objects.filter(title__icontains=keyword)

    return render(request, 'article/article_list.html', {'article_list': qs, 'q': keyword})


def detail(request, id):
    q = Article.objects.get(id=id)
    return render(request, 'article/article_detail.html', {'article': q})


article_list2 = None

article_new = None

article_edit = None

article_delete = None
