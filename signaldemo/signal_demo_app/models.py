from django.db import models

# Create your models here.

class UserProfile(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    username = models.CharField(max_length=150, primary_key=True)
    email = models.EmailField()
    created_by = models.DateTimeField(auto_now=True)
    updated_by = models.DateTimeField(auto_now_add=True)

    def full_name(self):
        return self.first_name + " " + self.last_name;

class Book(models.Model):
    author = models.ManyToManyField(UserProfile)
    title = models.CharField(max_length=250)
