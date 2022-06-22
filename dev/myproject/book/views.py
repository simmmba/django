from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView
from .models import Book
from .forms import BookForm

# book_new = CreateView.as_view(model=Book, fields='__all__')
book_list = ListView.as_view(model=Book)


def book_new(request):
    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            # 새로운 데이터 생성
            print(form.cleaned_data)
            # book = Book(**form.cleaned_data)
            # book.save()
            book = Book.objects.create(**form.cleaned_data)
            return redirect('/book/')

    elif request.method == 'GET':
        form = BookForm()

    return render(request, 'book/book_form2.html', {'form': form})


def book_edit(request, id):
    pass
