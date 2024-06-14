from django.db import models

# Create your models here.


class FirstTodo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=100)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
