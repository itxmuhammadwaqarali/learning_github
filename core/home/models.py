from django.db import models

# Create your models here.

class color(models.Model):
    name  = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Person(models.Model):
    colors = models.ForeignKey(color, null = True, blank=True, on_delete=models.CASCADE, related_name='color')
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    def __str__(self):
        return self.name  