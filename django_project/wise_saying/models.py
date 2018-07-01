from django.db import models

# Create your models here.

class Member(models.Model):
    member_id = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=40)
    name = models.CharField(max_length=16)

class Saying(models.Model):
    member = models.ForeignKey(Member, on_delete = models.CASCADE)
    contents = models.CharField(max_length = 200)

class Like(models.Model):
    member = models.ForeignKey(Member, on_delete = models.CASCADE)
    saying = models.ForeignKey(Saying, on_delete = models.CASCADE)
