from django.db import models

# Create your models here.
class Book(models.Model):
    bk_name = models.CharField(max_length=100)
    bk_number = models.IntegerField(null=True)

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title