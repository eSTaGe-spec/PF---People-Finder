from django.urls import path

from .views import AllTaskAPIView, TaskInfoAPIView, TaskAPIView, accept_task, CreateTaskAPIView


urlpatterns = [
    path('all_task/', AllTaskAPIView.as_view()),
    path('task/<int:task_id>/', TaskInfoAPIView.as_view()),
    path('task_profile/<int:user_id>/', TaskAPIView.as_view()),
    path('accept_task/<int:task_id>/', accept_task),
    path('create_task/', CreateTaskAPIView.as_view())
]
