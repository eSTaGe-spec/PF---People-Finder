# Generated by Django 4.2.11 on 2024-05-06 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0002_profile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='work_experience',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Опыт работы'),
        ),
    ]
