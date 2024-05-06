from django.contrib import admin

from .models import Profile, Skills


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email')
    list_display_links = ('name', )
    search_fields = ('user', 'email')


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_display_links = ('title', )
    search_fields = ('title', )

