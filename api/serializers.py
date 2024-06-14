from rest_framework import serializers
from .models import FirstTodo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstTodo
        fields = ['title', 'description', 'status', 'deadline', 'created_at']
