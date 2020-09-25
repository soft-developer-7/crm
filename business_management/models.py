from django.db import models
from tasks.models import User_db

# Create your models here.
class Packs(models.Model):
    title = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='package/',null=True,blank=True)
    plan = models.CharField(max_length=3000)
    validity = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Industries(models.Model):
    name = models.CharField(max_length=300)
    owner = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='industry/',null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




class Templates(models.Model):
    name = models.CharField(max_length=300)
    code = models.CharField(max_length=50)
    pack = models.ForeignKey(Packs, on_delete=models.CASCADE)
    ind = models.ForeignKey(Industries, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class User_bookings(models.Model):

    title = models.CharField(max_length=300)
    user = models.ForeignKey(User_db, on_delete=models.CASCADE)
    template = models.ForeignKey(Templates, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title