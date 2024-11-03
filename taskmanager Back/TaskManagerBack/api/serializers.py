# serializers.py
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'  # or specify each field explicitly, e.g., ('id', 'title', 'description', 'due_date', 'status', 'created_at')
        def update(self, instance, validated_data):
            instance.status = validated_data.get('status', instance.status)
            instance.save()
            return instance