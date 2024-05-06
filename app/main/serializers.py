from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Task, Tag


class TaskSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        slug_field='title'
    )
    created_by_profile = serializers.StringRelatedField(source='created_by.profile.name')
    assigned_by_profile = serializers.StringRelatedField(source='assigned_to.profile.name')

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'tags', 'price', 'created_by_profile', 'assigned_by_profile',
                  'is_quickly']


class TaskProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['title', 'id']


