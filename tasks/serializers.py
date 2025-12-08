from rest_framework import serializers
from .models import Task



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '--all--'
        read_only_fields =['owner']
        