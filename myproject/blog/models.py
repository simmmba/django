from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_at = models.DateField(auto_now_add=True) # 수정불가
    updated_at = models.DateTimeField(auto_now=True) # 수정가능

    def __str__(self):
        return self.title