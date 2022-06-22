from django.urls import path, register_converter
from . import views
from .converters import CodeConverter

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='list'),
    path('<int:post_id>/', views.detail),
    # path('archives/<dddd:code>/', views.blog_code),
    path('json/', views.json_test),
    path('file/', views.excel_download),
    path('redirect/', views.get_redirect),
]
