from rest_framework import serializers

from .models import Profile, Skills


class ProfileShortSerializer(serializers.ModelSerializer):
    skills = serializers.SlugRelatedField(
        many=True,
        queryset=Skills.objects.all(),
        slug_field='title'
    )

    class Meta:
        model = Profile
        fields = ['id', 'name', 'age', 'work_experience', 'avatar', 'skills']


class ProfileSerializer(serializers.ModelSerializer):
    skills = serializers.SlugRelatedField(
        many=True,
        queryset=Skills.objects.all(),
        slug_field='title'
    )

    class Meta:
        model = Profile
        fields = ['id', 'name', 'age', 'work_experience', 'phone_number', 'email', 'skills', 'avatar']


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ['title', 'id']
