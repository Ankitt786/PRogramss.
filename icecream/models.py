from django.db import models


# Create your models here.
class Contact(models.Model):
    firstname=models.CharField(max_length=120)
    lastname=models.CharField(max_length=120)
    email=models.CharField(max_length=120)
    phone=models.CharField(max_length=120)
    # textarea=models.CharField(max_length=122)

# this fuction we can change the name in data-base! SS
    def __str__(self):
        return self.firstname

    


