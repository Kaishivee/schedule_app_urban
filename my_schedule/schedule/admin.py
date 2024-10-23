from django.contrib import admin
from .models import Lesson, Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'day_of_week', 'date', 'time', 'classroom')
    list_filter = ('group', 'day_of_week')
    search_fields = ('name', 'group__name')
