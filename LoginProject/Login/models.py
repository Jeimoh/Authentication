from django.db import models




# Create your models here.
class Users(models.Model):
    Userid = models.CharField(primary_key=True, max_length = 20)
    password = models.CharField(max_length=128)  # Define a CharField for the password
    Email = models.EmailField()
    Username = models.CharField(max_length = 50)
    phoneNo = models.CharField(max_length = 15)

  
    def __str__(self):
        return self.Username


