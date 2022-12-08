from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField('Name', max_length=50)
    task = models.TextField('description')

    def __str__(self):
        return self.title
