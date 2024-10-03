from django.contrib import admin
from . import  models

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    exclude = ['id','priority_order','created_at','completed']
    list_display = ('title', 'priority', 'completed', 'created_at')  # Fields to display in the list view
    list_filter = ('priority', 'completed')  # Filters to the right of the list
    search_fields = ('title', 'description')  # Fields to search

# Register the Task model with the custom TaskAdmin
admin.site.register(models.Task, TaskAdmin)
admin.site.register(models.Category)
