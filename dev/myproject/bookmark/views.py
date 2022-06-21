from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Bookmark


# bookmark_list = ListView.as_view(model=Bookmark)
# bookmark_detail = DetailView.as_view(model=Bookmark)

def bookmark_list(req):
    bookmark_list = Bookmark.objects.all()
    return render(req, 'bookmark/bookmark_list.html', {'bookmark_list': bookmark_list})


def bookmark_detail(req, pk):
    bookmark = get_object_or_404(Bookmark, id=pk)
    return render(req, 'bookmark/bookmark_detail.html', {'bookmark': bookmark})
