from django.shortcuts import render
from django.http import HttpResponse

def index(req):
    # 서버 서비스 처리
    
    return HttpResponse("Hello Python")