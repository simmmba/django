from django import forms
from django.core.exceptions import ValidationError
from .models import Book


def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력해주세요')


class BookForm(forms.Form):
    title = forms.CharField(label='제목')
    author = forms.CharField(label='저자', validators=[min_length_3_validator])
    publisher = forms.CharField(label='출판사', required=False)

    def save(self, commit=True):
        book = Book(**self.cleaned_data)
        if commit:
            book.save()
        return book


class BookModelForm(forms.ModelForm):
    # ModelForm 안에 save() 포함되어있음
    class Meta:
        model = Book
        # fields = '__all__'  # 모든 모델값을 필드값으로
        fields = ['title', 'author', 'publisher']

    def clean_author(self):
        author = self.cleaned_data.get(
            'author', '')  # author 존재하지 않으면 '' return
        if author:
            if len(author) < 3:
                raise ValidationError('최소 3글자 이상 입력하세요.')  # 오류 발생
        return author

    def clean(self):
        data = self.cleaned_data
        print(data)
        # self. 붙여야 class 내부에서 호출함
        if self.check_exist(data.get('title'), data.get('author')):  # key값이 없어도 오류 X
            raise ValidationError('이미 등록된 책입니다.')
        return data

    def check_exist(self, title, author):
        return Book.objects.filter(title=title, author=author).exists()
