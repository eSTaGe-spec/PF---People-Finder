from django.urls import path

from .views import ProfileAPIView, LoginAPIView, RegisterAPIView, UserInfoAPIView, SkillsAPIView

urlpatterns = [
    path('profile/', ProfileAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('register/', RegisterAPIView.as_view()),
    path('user_settings/', UserInfoAPIView.as_view()),
    path('skills/', SkillsAPIView.as_view())
]
