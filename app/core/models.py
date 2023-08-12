"""
Model for core app.
"""

from django.db import models


class Student(models.Model):
    """
    Student model.
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='image/')
    age = models.IntegerField()
    email = models.EmailField(unique=True,default=None)
    contact = models.CharField(max_length=10)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name