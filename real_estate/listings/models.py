from django.db import models

# Create your models here.
class Listing(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    num_bedrooms = models.IntegerField()
    square_footage = models.IntegerField()
    address = models.CharField(max_length=250)
    # image
    
    def __str__(self):
        return f"{self.title}"