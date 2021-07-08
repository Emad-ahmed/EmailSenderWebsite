from django.shortcuts import render
from django.views import View
from leapp.models import Contact
from leapp.forms import SignUpForm, UpdateSignForm
from django.contrib import messages
# Create your views here.


class SettingView(View):
    def get(self, request):
        id = request.session.get('myid')
        pi = Contact.objects.get(pk=id)
        form = UpdateSignForm(instance=pi)
        mydata = {
            'settings': 'active',
            'form': form
        }
        return render(request, 'setting.html', mydata)

    def post(self, request):

        id = request.session.get('myid')
        pi = Contact.objects.get(pk=id)
        form = UpdateSignForm(request.POST, instance=pi)

        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Saved!")

        mydata = {
            'settings': 'active',
            'form': form
        }
        return render(request, 'setting.html', mydata)
