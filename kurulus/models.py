from unittest.util import _MAX_LENGTH
from django.db import models
from enum import Enum
from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractUser


SAHIS = "SH"
KOBI = "KO"
STK = "STK"
BUYUK_ISLETME = "BI"
KurulusChoice = [
    (SAHIS, "Sahsi"),
    (STK, "STK"),
    (KOBI, "KOBI"),
    (BUYUK_ISLETME, "BI")
]

class Kurulus(models.Model):   
    KurulusId = models.AutoField(primary_key=True),
    KurulusAdi = models.CharField(max_length=20),
    KurulusLogo = models.ImageField(upload_to ='uploads/'),
    KurulusUlke = CountryField()
    KurulusUrl = models.URLField(max_length = 200)
    KurulusTuru = models.CharField(
        max_length=10,
        choices=KurulusChoice,
        default=SAHIS,
    )

    KurukusCalisanSayi = models.IntegerField()
    
    # import your Models and Enums
    # b = Book(title='Deutsch Für Ausländer', language=LanguageChoice.DE)
    # b.save()



# Create your models here.
# class User(AbstractUser):
#     name = models.CharField(max_length=255)
#     email = models.CharField(max_length=255, unique=True)
#     password = models.CharField(max_length=255)
#     username = None

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []