from django.db import models
from django.contrib.auth.models import User


class Discussion(models.Model):
    title = models.CharField(max_length=255)
    starter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="started_discussions")
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.title


class Post(models.Model):
    content = models.TextField(max_length=5000)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chat_posts")
    created_at = models.DateTimeField(auto_now_add=True)
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return f"{self.author.username} - {self.content[:20]}"
