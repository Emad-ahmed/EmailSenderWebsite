from django.db import models
from django.db.models.aggregates import Max
from django.db.models.base import Model


class Contact(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    insta_acc = models.URLField(max_length=200)
    phone = models.IntegerField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.username

    @staticmethod
    def myuser(self):
        return Contact.objects.filter(username=self.username)
