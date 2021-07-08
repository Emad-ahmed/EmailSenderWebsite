from django.shortcuts import render
from django.views import View
from leapp.forms import SignUpForm
from django.contrib import messages
# Create your views here.


class SignupView(View):
    def get(self, request):

        fm = SignUpForm()
        mydata = {
            'signup': 'active',
            'form': fm
        }
        return render(request, 'signup.html', mydata)

    def post(self, request):
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Successfully Saved!")
        return render(request, 'signup.html', {'form': fm})
