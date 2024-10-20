from typing import Iterable
from django.db import models
from django.db.models import Q
from django.core.exceptions import ValidationError

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
    submitted = models.IntegerField(default=0)
    
    
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
    
class registrations(models.Model):
    event = models.ForeignKey(events, on_delete=models.CASCADE)
    
    teamname = models.CharField(max_length=100)
    
    mem1 = models.CharField(max_length=200)
    roll1 = models.CharField(max_length=100)
    
    mem2 = models.CharField(max_length=200)
    roll2 = models.CharField(max_length=100)
    
    mem3 = models.CharField(max_length=200)
    roll3 = models.CharField(max_length=100)
    
    mem4 = models.CharField(max_length=200)
    roll4 = models.CharField(max_length=100)
    
    contact = models.CharField(max_length=20)
    
    def clean(self):
        duplication = registrations.objects.filter(event=self.event)
        def is_roll_duplicate(new_roll, existing_rolls):
            return new_roll and new_roll in existing_rolls
         
        for entry in duplication:
            existing_rolls = [entry.roll1, entry.roll2, entry.roll3]
            if (is_roll_duplicate(self.roll1, existing_rolls) or 
                is_roll_duplicate(self.roll2, existing_rolls) or
                is_roll_duplicate(self.roll3, existing_rolls)):
                print(existing_rolls)
                raise ValidationError("Registration Duplication")
    
    def save(self, *args, **kwargs):
        self.clean()
        return super().save(*args,**kwargs)
        
    
    def __str__(self):
        return self.event.name
    
    class Meta:
        verbose_name = "Registration"
        verbose_name_plural = "Registrations"
        
class hackathonreg(registrations):
    statement = models.ForeignKey(statements,  on_delete=models.CASCADE)
    
    def clean(self):
        duplication = hackathonreg.objects.filter(event=self.event)
        def is_roll_duplicate(new_roll, existing_rolls):
            return new_roll and new_roll in existing_rolls
         
        for entry in duplication:
            existing_rolls = [entry.roll1, entry.roll2, entry.roll3, entry.roll4]
            if (is_roll_duplicate(self.roll1, existing_rolls) or 
                is_roll_duplicate(self.roll2, existing_rolls) or
                is_roll_duplicate(self.roll3, existing_rolls) or
                is_roll_duplicate(self.roll4, existing_rolls)):
                print(existing_rolls)
                raise ValidationError("Registration Duplication")
    
    def save(self, *args, **kwargs):
        self.clean()
        print(super())
        return super().save(*args,**kwargs)
    
    class Meta:
        verbose_name = "Hackathon Registration"
        verbose_name_plural = "Hackathon Registrations"
        
    def __str__(self):
        return self.statement.title
    