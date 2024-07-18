from django.contrib import admin
from .models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'due_date', 'due_time', 'completed', )
    search_fields = ['title', 'description', 'due_date', 'due_time', 'completed']


admin.site.register(Task,TaskAdmin)