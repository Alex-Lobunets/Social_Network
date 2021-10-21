from rest_framework import serializers
from .models import Post, Like
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'

        extra_kwargs = {'author': {'required': False}}

    def to_internal_value(self, data):
        dict_data = super(PostSerializer, self).to_internal_value(data)
        dict_data['author'] = self.context['request'].user
        return dict_data


class LikeAnalyticsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ('liked_at', 'user', 'post')
