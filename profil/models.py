from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class UserExtend(models.Model):
    #username = models.OneToOneField(User, on_delete='', unique=True, blank=True, null=True)
    #slug = models.CharField(max_length=100, default='fjasdlk', blank=True, unique=True)

    username = models.CharField(max_length=150, blank=True, unique=True, null=True)


    phone = models.CharField(max_length=100, blank=True)

    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)

    street = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    PSC = models.CharField(max_length=100, blank=True)

    img = models.ImageField(default='profil-img.png')

    created = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.username
