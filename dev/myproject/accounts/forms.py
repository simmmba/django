from django import forms
from django.core.validators import validate_email
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile


class SignupForm(UserCreationForm):
    phone_number = forms.CharField()
    address = forms.CharField()

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

    # save 함수 재정의
    def save(self):
        user = super().save()
        Profile.objects.create(
            user=user, phone_number=self.cleaned_data['phone_number'], address=self.cleaned_data['address'])
        return user

    # username이 email형태인지 검증
    def clean_username(self):
        value = self.cleaned_data.get('username')
        if value:
            validate_email(value)
        return value
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['username'].validators = [validate_email]

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.email = user.username
    #     if commit:
    #         user.save()
    #     return user


class LoginForm(AuthenticationForm):
    answer = forms.IntegerField(label='손흥민의 등번호는?')

    def clean_answer(self):
        answer = self.cleaned_data.get('answer', None)
        if answer != 7:
            raise forms.ValidationError('Wrong Answer!')
        return answer
