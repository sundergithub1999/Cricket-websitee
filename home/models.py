from datetime import date
import email
from email import message
from unicodedata import name
from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    message=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name

        


class Fee(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    Amount=models.CharField(max_length=12)
    message=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name



class Player(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    profession=models.CharField(max_length=122)
    message=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name



class Trainer(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    expert=models.CharField(max_length=122)
    message=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name
