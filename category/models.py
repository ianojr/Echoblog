# from django.db import models

# # Create your models here.
# class Category(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)


from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
