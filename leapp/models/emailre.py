from django.db import models
from leapp.models import Contact


class EmailSender(models.Model):
    user = models.ForeignKey(Contact, on_delete=models.CASCADE)
    from_email = models.EmailField()
    to_email = models.EmailField()
    subject = models.CharField(max_length=300, blank=True)
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)
    document = models.FileField(upload_to='documents/', blank=True)
