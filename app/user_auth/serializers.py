from rest_framework import serializers

from .models import Profile, Skills


class ProfileSerializer(serializers.ModelSerializer):
    skills = serializers.SlugRelatedField(
        many=True,
        queryset=Skills.objects.all(),
        slug_field='title'
    )

    class Meta:
        model = Profile
        fields = ['name', 'age', 'work_experience', 'phone_number', 'email', 'skills', 'avatar']


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ['title', 'id']
