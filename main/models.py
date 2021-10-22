from django.db import models

# Create your models here.
class Users(models.Model):
  username = models.CharField(max_length=50)
  email = models.EmailField(max_length=100)

  def __str__(self):
      return self.username  
