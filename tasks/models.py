from django.db import models


class Task(models.Model):
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=12, default='Pendente')
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
