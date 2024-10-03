from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.

class PrayerTime(models.Model):
    name = models.CharField(max_length=10)
    azan = models.CharField(max_length=10)
    prayer = models.CharField(max_length=10)
    icon = models.TextField()

    def __str__(self):
        return self.name
    

class Event(models.Model):
    name = models.CharField(max_length=50)
    start = models.DateTimeField()
    end = models.DateTimeField()
    venue = models.CharField(max_length=50)
    info = models.CharField(max_length=1000)
    picture = models.ImageField(blank=True, null=True, upload_to='media')
    slugger = models.SlugField()

    def __str__(self):
        return self.name
    

class Address(models.Model):
    number = models.CharField(max_length=20)
    street = models.CharField(max_length=50, blank=True, null=True)
    lga = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    days_active = models.CharField(max_length=50)
    longitude = models.FloatField()
    latitude = models.FloatField()    


    def __str__(self):
        return f'Mosque at {self.lga}'


class Service(models.Model):
    name = models.CharField(max_length=20)
    start = models.TimeField(null=True, blank=True)
    end = models.TimeField(null=True, blank=True)
    days = models.CharField(max_length=50, null=True, blank=True)


    def __str__(self):
        return f'{self.name} service.'
    
class Photo(models.Model):
    picture = models.ImageField(upload_to='media/photos')
    description = models.TextField()

    def __str__(self):
        return f'{self.description}'
    
class Email(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
    
class Message(models.Model):
    title = models.CharField(max_length=50)
    message = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return f'Message from {self.email} on {self.title}'
    
class Mosque(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mosque = models.ForeignKey(Address, on_delete=models.CASCADE, default=1)
    zoom = models.FloatField(default=10.00)
    from_zoom = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} mosque object'

class MosqueName(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Leader(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='media/photos')
    bio = models.TextField()

    def __str__(self):
        return f'{self.position} {self.name}'
    
class Download(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()
    file = models.FileField(upload_to='documents')

    def __str__(self):
        return self.name
    
class BankAccount(models.Model):
    account_name = models.CharField(max_length=50)
    account_number = models.CharField(max_length=11)
    bank_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.bank_name} account'