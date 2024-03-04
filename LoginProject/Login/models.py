from django.db import models




# Create your models here.
class User(models.Model):
    # Userid = models.CharField(primary_key=True, max_length = 20) # you don't need this, as this is auto-created
    username = models.CharField(max_length = 50)
    email = models.EmailField()
    phone = models.CharField(max_length = 15)
    password = models.CharField(max_length=128)  # Define a CharField for the password # passwords ought to have a hashing functionality

  
    def __str__(self):
        return self.username


