from django.db import models
from django.conf import settings
# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    degree1 = models.CharField(max_length=10)
    major1 = models.CharField(max_length=30)
    degree2 = models.CharField(max_length=10)
    major2 = models.CharField(max_length=30)
    degree3 = models.CharField(max_length=10)
    major3 = models.CharField(max_length=30)
    previous_experience = models.IntegerField()
    previous_profession = models.CharField(max_length=12)
    colg_cmpny_name = models.CharField(max_length=100)
