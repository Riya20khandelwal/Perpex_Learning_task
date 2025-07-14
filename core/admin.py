from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_on', 'updated_at', 'completed')
    search_fields = ('title',)

admin.site.register(Task, TaskAdmin)
