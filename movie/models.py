from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField('Movie Name', max_length=255,unique=True)
    description = models.TextField(verbose_name="Movie Description")
    likes = models.IntegerField(default=0)
    watch_count = models.IntegerField(default=0)
    rate = models.PositiveIntegerField(default=0)
    production_date = models.DateTimeField(null=True)
    creation_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category',on_delete=models.CASCADE,null=True,blank=True)
    actors = models.ManyToManyField('Cast')
    image = models.ImageField(upload_to='moviepic/')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name


class Cast(models.Model):
    actor = models.CharField(max_length=25)

    def __str__(self):
        return self.actor
