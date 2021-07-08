from django.core.checks import messages
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.views import View
from leapp.models import Contact
from django.contrib import messages
# Create your views here.


class LoginView(View):
    def get(self, request):
        mydata = {
            'login': 'active'
        }
        return render(request, 'login.html', mydata)

    def post(self, request):
        try:
            mydata = {
                'login': 'active'
            }
            email = request.POST.get('email')
            username = request.POST.get('username')

            customer = Contact.objects.filter(email=email)
            myuser = Contact.objects.filter(username=username)
            myuserid = Contact.objects.get(email=email)
            myid = myuserid.id

            if customer:
                request.session['myemail'] = email
                request.session['myid'] = myid
                if myuser:
                    return redirect('/')
                else:
                    messages.warning(request, 'Email or Password Invalid')
                    return render(request, 'login.html', mydata)
            else:
                messages.warning(request, 'Email or Password Invalid')
                return render(request, 'login.html', mydata)
        except:
            mydata = {
                'login': 'active'
            }
            messages.warning(request, 'Email or Password Invalid')
            return render(request, 'login.html', mydata)


def user_logout(request):
    request.session.flush()
    return HttpResponseRedirect('/login')
