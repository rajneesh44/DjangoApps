from django.db import models

# Create your models here.
class TodoItems(models.Model):
    content = models.TextField()