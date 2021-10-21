from dataclasses import dataclass

from .models import Post, Like
from django_filters import rest_framework as filters

from django.contrib.auth import get_user_model
CustomUser = get_user_model()


@dataclass
class PostService:

    user: object
    post_id: int

    def like_post(self) -> None:
        post = Post.objects.get(id=self.post_id)
        post.like.add(self.user)
        post.save()

    def unlike_post(self) -> None:
        post = Post.objects.get(id=self.post_id)
        post.like.remove(self.user)
        post.save()


class LikeByDateFilter(filters.FilterSet):
    date_from = filters.DateFilter(field_name='liked_at', lookup_expr='gt')
    date_to = filters.DateFilter(field_name='liked_at', lookup_expr='lt')

    class Meta:
        model = Like
        fields = ['liked_at', ]
