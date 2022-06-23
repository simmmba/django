from django.urls import path
from django.views.generic import ListView
from . import views
from .models import Article

app_name = 'article'
urlpatterns = [
    # path('', ListView.as_view(model=Article), name='list'),
    # path('', views.article_list, name='list'),
    path('', views.MyListView.as_view(), name='list'),
    path('<id>/detail/', views.detail, name='detail'),
    path('new/', views.article_new, name='new'),
    path('<pk>/edit/', views.article_edit, name='edit'),
    path('<pk>/delete/', views.article_delete, name='delete'),
]
