from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Profile, Skills
from .serializers import ProfileSerializer, SkillsSerializer, ProfileShortSerializer


class ProfileAPIView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        info = Profile.objects.get(user=user)
        serializer = ProfileSerializer(info)

        return Response(serializer.data, status=status.HTTP_200_OK)


class LoginAPIView(APIView):
    def post(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)

        if user is None:
            return Response({'error': 'Неверные учетные данные'}, status=status.HTTP_400_BAD_REQUEST)

        login(request=request, user=user)
        return Response(status=status.HTTP_200_OK)


class RegisterAPIView(APIView):
    def post(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        name = data.get('name')

        if not all([username, password]):
            return Response({'error': 'Все поля обязательны для заполнения'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Пользователь с таким именем уже существует'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password)
        user.save()
        Profile.objects.create(user=user, name=name)
        login(request=request, user=user)

        return Response(status=status.HTTP_201_CREATED)


class UserInfoAPIView(APIView):
    def get(self, request):
        info = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(info)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        user = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SkillsAPIView(APIView):
    def get(self, request):
        skills = Skills.objects.all()
        serializer = SkillsSerializer(skills, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UsersInfoAPIView(APIView):
    def get(self, request):
        users = Profile.objects.all()
        serializer = ProfileShortSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

