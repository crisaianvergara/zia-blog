from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    image_url = models.URLField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    date_commented = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f"{self.comment_text[:20]} - {self.author.username}"


class Reply(models.Model):
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name="replies"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    reply_text = models.TextField()
    date_replied = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f"Reply by {self.author.username} to {self.comment}"
