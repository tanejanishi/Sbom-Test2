#from django.test import TestCase

# Create your tests here.
from django.db import models
from django.db.models.query import QuerySet
from blog.models import Post

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Publisher(models.Model):
    name = models.CharField(max_length=300)

class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField()

class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)

class PublisherQuerySet(QuerySet):

    Q = QuerySet.aggregate(Post.ordering)
    q = QuerySet.annotate(Post.ordering)

    def drafts(self):
        return self.filter(publisher_is_draft=True)

    def public(self):
        return self.filter(publisher_is_draft=False)

