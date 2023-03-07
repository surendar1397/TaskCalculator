from django.db import models

# Create your models here.

class Question1(models.Model):
    Question = models.CharField(max_length=100)
    