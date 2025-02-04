# models.py
from django.db import models

class Contact(models.Model):
    
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    email = models.EmailField()
    massage = models.TextField()
    
    def __str__(self):
        return self.name
