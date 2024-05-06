from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .models import Tag, Task
from .serializers import TagSerializer, TaskSerializer, TaskProfileSerializer


class AllTaskAPIView(APIView):
    def get(self, request):
        task = Task.objects.all()
        serializer = TaskSerializer(task, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class TaskInfoAPIView(APIView):
    def get(self, request, task_id):
        task = Task.objects.get(pk=task_id)
        serializer = TaskSerializer(task)

        return Response(serializer.data, status=status.HTTP_200_OK)


class TaskAPIView(APIView):
    def get(self, request, user_id):
        created_tasks = Task.objects.filter(created_by=user_id)
        assigned_tasks = Task.objects.filter(assigned_to=user_id)

        created_tasks_serializer = TaskProfileSerializer(created_tasks, many=True)
        assigned_tasks_serializer = TaskProfileSerializer(assigned_tasks, many=True)

        return Response({
            'created_tasks': created_tasks_serializer.data,
            'assigned_tasks': assigned_tasks_serializer.data
        }, status=status.HTTP_200_OK)


class CreateTaskAPIView(APIView):
    def get(self, request):
        tag = Tag.objects.all()
        serializer = TagSerializer(tag, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def accept_task(request, task_id):
    if request.method == "POST":
        try:
            task = Task.objects.get(id=task_id)
            user_id = request.user.id
            task.assigned_to = User.objects.get(id=user_id)
            task.save()

            return JsonResponse({'status': 'success'}, status=200)
        except Exception as e:
            return JsonResponse({'status': 'error', 'error': str(e)}, status=400)
    else:
        return JsonResponse({'status': 'error', 'error': 'invalid method'})

