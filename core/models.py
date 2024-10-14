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
        return super().save(*args,**kwargs)
    
    class Meta:
        verbose_name = "Problem Statement"
        verbose_name_plural = "Problem Statements"
        
    def __str__(self) -> str:
        return self.title
    

class events(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField()
    time = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    venue = models.CharField(max_length=50)
    
    maxsub = models.IntegerField(default=200)
    statustext = models.CharField(max_length=75)
    isClosed = models.BooleanField(default=False)
    
    bgcolor = models.CharField(max_length=20)
    redirectURI = models.CharField(max_length=20)
    imageurl = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name