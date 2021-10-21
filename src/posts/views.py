from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Post, Like
from .serializers import PostSerializer, LikeAnalyticsSerializer
from .services import PostService, LikeByDateFilter


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=['post'], url_path='post-like', url_name='post_like')
    def post_like(self, request, pk):
        service = PostService(request.user, pk)
        service.like_post()
        return Response()

    @action(detail=True, methods=['delete'], url_path='post-unlike', url_name='post_unlike')
    def post_unlike(self, request, pk):
        service = PostService(request.user, pk)
        service.unlike_post()
        return Response()


class LikeAnalyticsViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeAnalyticsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = LikeByDateFilter
