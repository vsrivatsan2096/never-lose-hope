from django.db import models

# Create your models here.


class Job(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    branch = models.CharField(max_length=3)
    description = models.CharField(max_length=150)
    req_deg = models.CharField(max_length=10)
    req_major = models.CharField(max_length=30)


class Candidates(models.Model):
    id = models.AutoField(primary_key=True)
    job_id = models.IntegerField(default=0)
    user_id = models.IntegerField(default=0)
    status = models.CharField(max_length=20, default="Waiting")

