from django.contrib import admin
from .models import Post, Comment, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content_size',
                    'updated_at']  # 리스트에 보여줄 항목 설정
    list_display_links = ['id', 'title']  # 링크 항목 설정
    fields = ['title', 'content']  # 보여질 세부항목 설정
    search_fields = ['title', 'content']  # 검색 대상 설정
    list_filter = ['create_at']  # 필터링 구분값 설정

    def content_size(self, post):
        return '{}글자'.format(len(post.content))


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
