from django.db import models

# Create your models here.

class TodoModel(models.Model):
  title = models.CharField(max_length=255)
  is_done = models.BooleanField(default=False)