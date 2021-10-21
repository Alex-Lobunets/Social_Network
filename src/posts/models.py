from django.db import models
from django.conf import settings


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    body = models.TextField()
    like = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='likes',
        blank=True,
        through='Like'
    )

    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='liked_user'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='liked_post'
    )
    liked_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Liked post{self.post} by {self.user}'
