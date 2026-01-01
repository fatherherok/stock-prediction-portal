from django.db import models

# Create your models here.

class Destination(models.Model):
    # No need for an explicit ID — Django automatically adds one
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.name
