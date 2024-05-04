from django.urls import path
from django.views.generic import TemplateView


app_name = 'frontend'

urlpatterns = [
    path('', TemplateView.as_view(template_name='frontend/index.html'), name='index'),
    path('task/', TemplateView.as_view(template_name='frontend/task.html'), name='task'),
    path('login/', TemplateView.as_view(template_name='frontend/login.html'), name='login'),
    path('register/', TemplateView.as_view(template_name='frontend/register.html'), name='register'),
    path('profile/', TemplateView.as_view(template_name='frontend/profile.html'), name='profile'),
    path('users/', TemplateView.as_view(template_name='frontend/users.html'), name='users'),
    path('create-order/', TemplateView.as_view(template_name='frontend/create-order.html'), name='create-order'),
    path('user-settings', TemplateView.as_view(template_name='frontend/user-settings.html'), name='user-settings'),
]

