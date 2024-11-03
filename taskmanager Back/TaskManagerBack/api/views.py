# views.py
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
import logging

logger = logging.getLogger(__name__)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):
        logger.info("Données reçues : %s", request.data)
        return super().create(request, *args, **kwargs)
    def update(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')  # Get task ID from URL
        logger.info("Updating Task ID: %s with data: %s", task_id, request.data)
        
        # Call the parent class update method
        return super().update(request, *args, **kwargs)