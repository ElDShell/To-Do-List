from typing import Any
from django.db import models

# Create your models here.
class Category(models.Model): 
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
    
class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    priority  = models.CharField(max_length=6,
        choices=[
        ('l', 'Low'),
        ('m', 'Medium'),
        ('h', 'High'),
    ])
    PRIORITY_ORDER = {
        'l': 1,
        'm': 2,
        'h': 3,
    }
    priority_order = models.IntegerField(editable=False)
    default='m'
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.id is None:
            last_task = Task.objects.order_by('id').last()
            self.id = last_task.id + 1 if last_task else 1
        self.priority_order = self.PRIORITY_ORDER.get(self.priority,2)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.reassign_ids()
        
    @classmethod
    def reassign_ids(cls):
        tasks =cls.objects.order_by('id')
        for index, task in enumerate(tasks, start=1):
            task.id = index
            task.save()
    class Meta:
        ordering = ['id']

        
