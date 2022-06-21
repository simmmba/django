from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class BlockedMiddleware(MiddlewareMixin):
    def process_request(self, request):
        blocked = request.session.pop('blocked', None)
        if blocked:
            messages.info(request, "다른 기기에서 동일 아이디로 로그인되어 자동으로 로그아웃 되었습니다.")
            auth_logout(request)
            return redirect(settings.LOGIN_URL)