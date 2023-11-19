from django.db import models


# class Director(models.Model):
#     name = models.CharField(max_length=100)
#     surname = models.CharField(max_length=100)
#     age = models.IntegerField()
#
#
# class Film(models.Model):
#     title = models.CharField(max_length=100)
#     year = models.DateField()
#     genre = models.CharField(max_length=100)
#     director = models.ForeignKey(Director, on_delete=models.CASCADE)
#
#
# class Country(models.Model):
#     name = models.CharField(max_length=100)
#
#
# class Product(models.Model):
#     name = models.CharField(max_length=50)
#     price = models.FloatField()
#     # image = models.ImageField(upload_to='static/images')
#     created_at = models.DateTimeField(auto_now_add=True)   # встановлюється 1 раз
#     modified_at = models.DateTimeField(auto_now=True)      # встановлюється при кожній зміні
#     country = models.ForeignKey(Country, on_delete=models.CASCADE)
#
#
# class Artist(models.Model):
#     name = models.CharField(max_length=50)
#     year = models.DateTimeField()
#
#
# class Albom(models.Model):
#     name = models.CharField(max_length=50)
#     year = models.DateTimeField()
#     # folder = models.ImageField(upload_to='static/images')
#     artist = models.ForeignKey(Artist, default=1, on_delete=models.SETDEFAULT)
#
#
# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     year = models.DateField()
#     author = models.CharField(max_length=100)


class Abstract(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Project(Abstract):
    pass


class Task(Abstract):
    status = models.BooleanField()
    deadline = models.DateTimeField()
    priority = models.IntegerField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
