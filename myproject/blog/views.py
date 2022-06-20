from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

def index(req):
    # 서버 서비스 처리
    res = "<h2>Hello Django</h2>"
    return HttpResponse(res)

def test(req):
    r = Post.objects.all()
    post_list = [item for item in r]
    return render(req, 'index.html', {'post_list':post_list})

def detail(req, no):
    post = get_object_or_404(Post, pk=no)
    return render(req, 'detail.html', {'post':post})