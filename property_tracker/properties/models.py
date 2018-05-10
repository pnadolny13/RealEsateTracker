from django.db import models

class PropertyDetails(models.Model):
    address = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    beds = models.DecimalField(max_digits=6, decimal_places=2)
    baths = models.DecimalField(max_digits=6, decimal_places=2)
    sqft = models.IntegerField(default=0)