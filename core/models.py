from typing import Iterable
from django.db import models

class statements(models.Model):
    difficulty_choices = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low')
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(choices=difficulty_choices, max_length=50)
    submissions = models.IntegerField(default=20)
    
    
    def save(self, *args, **kwargs):
        print("ssfd", *args, **kwargs)
        return super().save(*args,**kwargs)
    
    class Meta:
        verbose_name = "Problem Statement"
        verbose_name_plural = "Problem Statements"
        
    def __str__(self) -> str:
        return self.title