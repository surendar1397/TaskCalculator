from django.db import models

# Create your models here.

class Question(models.Model):
    Question = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    