from statistics import mode
from tkinter import CASCADE
from django.db import models
from pandas import notnull

# Create your models here.

class Post(models.Model):
    author = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    text = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=65)
    body = models.TextField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return (self.post.title) (self.name) 
