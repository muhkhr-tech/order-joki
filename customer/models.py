from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=300, unique=True)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    