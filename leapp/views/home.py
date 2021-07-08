
from django.shortcuts import render
from django.views import View
from leapp.models import Contact, EmailSender
from django.core.mail import send_mail
from django.contrib import messages
from django.core.mail import EmailMessage
# Create your views here.


class HomeView(View):
    def get(self, request):
        mydata = {
            'email': 'active'
        }

        return render(request, 'home.html', mydata)

    def post(self, request):
        user_email = request.session.get('myemail')
        main_user = Contact.objects.get(email=user_email)
        from_email = user_email
        to_my_email = request.POST.get('to_email')
        to_email = [to_my_email]
        subject = request.POST.get('subject')
        my_message = request.POST.get('my_message')
        file = request.FILES['file']

        my_email_sender = EmailSender(
            user=main_user, from_email=from_email, to_email=to_email, subject=subject, message=my_message, document=file)
        my_email_sender.save()

        email = EmailMessage(subject, my_message, from_email, to_email)
        email.content_subtype = 'html'

        email.attach(file.name, file.read(), file.content_type)
        email.send()

        messages.success(request, "Successfully Send Mail")

        mydata = {
            'email': 'active'
        }

        return render(request, 'home.html', mydata)
