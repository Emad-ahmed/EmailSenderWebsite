from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms import widgets
from leapp.models import Contact
from django import forms
from django.core import validators


class SignUpForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['f_name', 'l_name', 'insta_acc',
                  'phone', 'username', 'email']

        labels = {
            'f_name': 'First Name',
            'l_name': 'Last Name',
            'insta_acc': 'Instagram Account',
            'phone': 'Phone',
            'username': 'Username',
            'email': 'Email',
        }

        widgets = {'f_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'l_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'insta_acc': forms.URLInput(attrs={'class': 'form-control'}),
                   'phone': forms.NumberInput(attrs={'class': 'form-control'}),
                   'username': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}),
                   }

    def clean_email(self):
        email = self.cleaned_data['email']
        if Contact.objects.filter(email=email).exists():
            raise ValidationError("Email Already Exists")

        return email

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if Contact.objects.filter(phone=phone).exists():
            raise ValidationError("Phone Number Already Exists")

        return phone

    def clean_username(self):
        username = self.cleaned_data['username']
        if Contact.objects.filter(username=username).exists():
            raise ValidationError("Username Already Exists")
        return username


class UpdateSignForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['f_name', 'l_name', 'insta_acc',
                  'phone', 'username', 'email']

        labels = {
            'f_name': 'First Name',
            'l_name': 'Last Name',
            'insta_acc': 'Instagram Account',
            'phone': 'Phone',
            'username': 'Username',
            'email': 'Email',
        }

        widgets = {'f_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'l_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'insta_acc': forms.URLInput(attrs={'class': 'form-control'}),
                   'phone': forms.NumberInput(attrs={'class': 'form-control'}),
                   'username': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}),
                   }
