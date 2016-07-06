from django.contrib import admin

# Register your models here.
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at']
    search_fields = ['name', 'description']
    list_per_page = 2
    list_filter = ['created_at']

admin.site.register(Todo, TodoAdmin)