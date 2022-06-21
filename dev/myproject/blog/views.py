import os
from io import StringIO, BytesIO
from urllib.parse import quote
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, Http404, JsonResponse
from django.conf import settings
import pandas as pd
from .models import Post


def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', {'post_list': post_list})


def blog_code(request, code):
    return HttpResponse('{}코드에 대한 내용'.format(code))


def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/detail.html', {'post': post})


def json_test(request):
    music = {'singer': 'BTS', 'songs': ['FAKE LOVE', 'DNA', '피 땀 눈물', '봄날']}
    return JsonResponse(music, json_dumps_params={'ensure_ascii': False})


def excel_download(request):
    filepath = os.path.join(settings.BASE_DIR, 'demo.xlsx')
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel')
        response["Content-Disposition"] = "attachment; filename={}".format(
            filename)
    return response


def get_redirect(request):
    return redirect('http://google.com')
