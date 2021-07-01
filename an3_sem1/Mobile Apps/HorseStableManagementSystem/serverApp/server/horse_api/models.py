from django.db import models

class Horse(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    breed = models.CharField(max_length=255)
    food = models.CharField(max_length=255)
    disease = models.CharField(max_length=255)

    def __str__(self):
        return self.name
