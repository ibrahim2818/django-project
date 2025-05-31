from django.db import models
from django.contrib.auth.models import User
from .utils import user_directory_path

class Location(models.Model):
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128 , blank=True)
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=5)
class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField( upload_to=user_directory_path, null=True)
    bio= models.CharField(max_length=140, blank=True)
    phone_number= models.CharField(max_length=12, blank=True)
    location = models.OneToOneField(Location, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.user.username}\'s profile'

        # This method is called when you use the print() function or str() function on an object.
        # Here, it returns a formatted string using an f-string.
        # It accesses the 'user' attribute of the current 'Profile' object, which is expected to be a 'User' instance.
        # Then, it retrieves the 'username' attribute of the 'User' object, which is a string representing the user's username.
        # Finally, it returns a string in the format "<username>'s profile".
        #return f"{self.user.username}'s profile"
