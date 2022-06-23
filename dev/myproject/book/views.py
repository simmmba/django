from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView
from .models import Book
from .forms import BookForm, BookModelForm

# book_new = CreateView.as_view(model=Book, fields='__all__')
book_list = ListView.as_view(model=Book)


def book_new(request):
    if request.method == 'POST':
        # form = BookForm(request.POST)
        form = BookModelForm(request.POST)

        if form.is_valid():
            # 새로운 데이터 생성
            # print(form.cleaned_data)
            # book = Book(**form.cleaned_data)
            # book.save()
            # book = Book.objects.create(**form.cleaned_data)
            book = form.save(commit=False)  # commit 지연
            book.ip = request.META['REMOTE_ADDR']
            book.save()
            return redirect('/book/')

    # elif request.method == 'GET':
    else:  # POST 아니면 GET
        form = BookForm()

    return render(request, 'book/book_form2.html', {'form': form})


def book_edit(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        form = BookModelForm(request.POST, instance=book)  # book 객체 가져오기

        if form.is_valid():
            book = form.save(commit=False)
            book.ip = request.META['REMOTE_ADDR']
            book.save()
            return redirect('/book/')

    else:
        form = BookModelForm(instance=book)  # form에 book instance 담아보내기

    return render(request, 'book/book_form2.html', {'form': form})


def book_delete(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('/book/')
