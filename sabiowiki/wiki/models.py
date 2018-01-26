import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    category_type = models.CharField(max_length=100)
    slug          = models.SlugField(max_length=100)

    def __str__(self):
        return self.category_type

class Article(models.Model):
    title    = models.CharField(max_length=200)
    slug     = models.SlugField(max_length=100)
    content  = models.TextField()
    pub_date = models.DateTimeField('Data de publicacao')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now()-datetime.timedelta(days=1)
