# models.py
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('To_do', 'À faire'),
            ('In_Progress', 'En cours'),
            ('Done', 'Terminé')
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
