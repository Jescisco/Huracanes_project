from django.db import models

# Create your models here.
class Login(models.Model):
    user = models.CharField(max_length=200)
    #Actualizar a Password field
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.user
