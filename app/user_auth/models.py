from django.db import models
from django.contrib.auth.models import User


def profile_avatar_path(instance, filename):
    return 'profile/user_{pk}/avatar/{filename}'.format(
        pk=instance.user.pk,
        filename=filename
    )


class Skills(models.Model):
    title = models.CharField(max_length=100, verbose_name='Навыки')

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Юзер')
    name = models.CharField(max_length=255, null=True, verbose_name='Имя пользователя')
    age = models.IntegerField('Возраст', blank=True, null=True, default=0)
    work_experience = models.IntegerField('Опыт работы', blank=True, null=True, default=0)
    phone_number = models.CharField(max_length=11, blank=True, null=True, verbose_name='Номер телефона')
    email = models.EmailField('Емаил')
    skills = models.ManyToManyField(Skills, verbose_name='Навыки')
    avatar = models.ImageField(blank=True, null=True, upload_to=profile_avatar_path, verbose_name='Аватар')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


