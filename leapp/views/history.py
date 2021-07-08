from os import name
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from leapp.models import Contact, EmailSender
# Create your views here.


class HistoryView(View):
    def get(self, request):
        myallcontact = Contact.objects.all()

        mydata = {
            'history': 'active',
            'myuser': myallcontact
        }

        return render(request, 'history.html', mydata)


def showemail(request, id):

    myid = Contact.objects.get(pk=id)
    myuser = myid.username

    emailmain = EmailSender.objects.filter(user__username=myuser)

    return render(request, 'showemail.html', {"emailmain": emailmain})
