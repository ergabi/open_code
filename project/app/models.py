from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publish_date = models.DateField()
    page = models.IntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)

    