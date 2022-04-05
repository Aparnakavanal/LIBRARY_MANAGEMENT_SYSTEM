from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=100)
    published_date = models.DateField()
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    book_image = models.FileField(upload_to="images/")
    username = models.CharField(max_length=100,null=True)


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.CharField(max_length=100)


