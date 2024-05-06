from django.contrib import admin

from .models import Tag, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_by', 'assigned_to', 'price', 'is_quickly']
    list_display_links = ['title', ]
    search_fields = ['title', ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title', ]
    list_display_links = ['title', ]
