# Generated by Django 4.2.11 on 2024-05-04 17:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import user_auth.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Навыки')),
            ],
            options={
                'verbose_name': 'Навык',
                'verbose_name_plural': 'Навыки',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='Возраст')),
                ('work_experience', models.IntegerField(blank=True, null=True, verbose_name='Опыт работы')),
                ('phone_number', models.CharField(blank=True, max_length=11, null=True, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Емаил')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=user_auth.models.profile_avatar_path, verbose_name='Аватар')),
                ('skills', models.ManyToManyField(to='user_auth.skills', verbose_name='Навыки')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Юзер')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
    ]