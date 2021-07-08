from django.shortcuts import render
from django.views import View
# Create your views here.


class SubcriptionView(View):
    def get(self, request):
        mydata = {
            'subscription': 'active'
        }
        return render(request, 'subscription.html', mydata)
