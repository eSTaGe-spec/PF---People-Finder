from django.urls import path

from .views import ProfileAPIView, LoginAPIView, RegisterAPIView, UserInfoAPIView, SkillsAPIView, UsersInfoAPIView

urlpatterns = [
    path('profile/<int:user_id>/', ProfileAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('register/', RegisterAPIView.as_view()),
    path('user_settings/', UserInfoAPIView.as_view()),
    path('skills/', SkillsAPIView.as_view()),
    path('users_info/', UsersInfoAPIView.as_view())
]
