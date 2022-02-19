from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django import forms
from . import models

def register(request):
    #REGISTER A NEW USER
    if request.method != 'POST':
        #BLANK REGISTRATION FORM
        form = UserCreationForm()
    else:
        #COMPLETED FORM
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #LOG IN AND REDIRECT TO HOME PAGE
            login(request, new_user)
            return redirect('project:index')

    #BLANK OR INVALID FORM
    context = {'form': form}
    return render(request, 'registration/register.html', context)

class ProfileForm(forms.Form):
    first_name = forms.CharField(label='First name:', max_length=50)
    last_name = forms.CharField(label='Last name:', max_length=50)
    address_1 = forms.CharField(label='Address:', max_length=100)
    address_2 = forms.CharField(label='Address 2:', max_length=120,
        help_text='<br/>The apartment, suite, unit number, or other address designation.', 
        required=False)
    city = forms.CharField(label='City:', max_length=100)
    state = forms.ChoiceField(choices=models.USState.StatesChoices, label='State') # States model
    zipcode = forms.CharField(label='Zipcode', max_length=9)


def profile(request):
    if request.method != 'POST':
        form = ProfileForm()
    else: 
        form = ProfileForm(request.POST)
        if form.is_valid():
            return redirect('project:index')
    
    return render(request, 'profile_mgmt/profile_mgmt.html', {'profile_form': form})