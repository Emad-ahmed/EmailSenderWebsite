from django.contrib import admin
from leapp.models import Contact, EmailSender

# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']


@admin.register(EmailSender)
class EmailAdmin(admin.ModelAdmin):
    list_display = ['id', 'to_email']
