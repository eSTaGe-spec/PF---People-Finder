from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views

app_name = 'frontend'

urlpatterns = [
    path('', TemplateView.as_view(template_name='frontend/index.html'), name='index'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('task/<int:task_id>/', TemplateView.as_view(template_name='frontend/task.html'), name='task'),
    path('login/', TemplateView.as_view(template_name='frontend/login.html'), name='login'),
    path('register/', TemplateView.as_view(template_name='frontend/register.html'), name='register'),
    path('profile/<int:user_id>/', TemplateView.as_view(template_name='frontend/profile.html'), name='profile'),
    path('users/', TemplateView.as_view(template_name='frontend/users.html'), name='users'),
    path('create_task/', TemplateView.as_view(template_name='frontend/create_task.html'), name='create_task'),
    path('user_settings/', TemplateView.as_view(template_name='frontend/user-settings.html'), name='user_settings'),
]

