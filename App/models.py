from django.db import models


# Create your models here.
class Category(models.Model):
    objects = None
    name = models.CharField(max_length=100,null=False)


class Task(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    priority = models.IntegerField(default=1, primary_key=True)
    description = models.TextField()


class ImageUpload(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
