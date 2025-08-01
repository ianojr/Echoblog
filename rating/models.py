from django.db import models

from post.models import Post

# Create your models here.
class Rating(models.Model):
    stars = models.IntegerField()
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)