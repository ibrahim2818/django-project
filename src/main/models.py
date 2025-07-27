import uuid
from django.db import models
from users.models import Profile, Location
from .const import CAR_BRANDS, TRANSMISSION_OPTIONS
from .utils import user_listings_path
# Create your models here.
class Listing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE)
    brand = models.CharField(max_length=64, choices=CAR_BRANDS, default='toyota')
    model = models.CharField(max_length=64, default=None)
    vin = models.CharField(max_length=17, unique=True,)
    mileage = models.PositiveIntegerField(default=0)
    color = models.CharField(max_length=32, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    engine= models.CharField(max_length=64,default=None)
    Transmission = models.CharField(max_length=32, choices=TRANSMISSION_OPTIONS, default=None)
    location = models.OneToOneField(Location, on_delete=models.SET_NULL, blank=True, null=True)
    image= models.ImageField(upload_to=user_listings_path, blank=True, null=True)


    def __str__(self):
        
        return f"{self.seller.user.username} - {self.brand} {self.model} ({self.vin})"