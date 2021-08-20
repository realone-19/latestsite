from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    price = models.IntegerField()


    def __str__(self):
        return self.name


class Lead(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    estate_name = models.CharField(max_length=30)
    number_of_plots = models.IntegerField()
    home_address = models.CharField(max_length=30)
    office_address = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone_number = models.IntegerField()
    date = models.DateField(auto_now=True)
