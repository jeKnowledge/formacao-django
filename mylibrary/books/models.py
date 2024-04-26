from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    #genre = models.ManyToManyField(Genre)


    def __str__(self):
        return self.title