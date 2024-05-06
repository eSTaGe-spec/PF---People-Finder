from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    tags = models.ManyToManyField(Tag, verbose_name='Теги')
    price = models.IntegerField(verbose_name='Цена задания')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks_created',
                                   verbose_name='Пользователь, создавший задание')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='tasks_taken',
                                    verbose_name='Пользователь, взявший задание')
    is_quickly = models.BooleanField(default=False, verbose_name='Срочный заказ?')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

