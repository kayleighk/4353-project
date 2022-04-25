from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core import validators
from django.core.validators import RegexValidator
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


def log_in(request):
    #LOG IN A USER
    if request.method == 'POST':
    #COMPLETED FORM
        form = AuthenticationForm(request=request, data=request.POST)

        if form.is_valid():
            #GET INFO FROM FORM
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            #LOG IN AND REDIRECT TO HOME PAGE
            if user is not None: 
                login(request, user)
                return redirect('project:index')

    #INVALID LOGIN         
    form = AuthenticationForm()
    context = {'form': form}  
    return render(request, 'registration/login.html', context)  


def log_out(request):
    logout(request)
    return redirect('project:index')


class ProfileForm(forms.Form):
    # validate_slug is a Name validation regex, built into Django
    first_name = forms.CharField(label='First name:', max_length=50, validators=[validators.validate_slug])
    last_name = forms.CharField(label='Last name:', max_length=50, validators=[validators.validate_slug])

    address_1 = forms.CharField(label='Address:', max_length=100)
    address_2 = forms.CharField(label='Address 2:', max_length=120,
        help_text='<br/>The apartment, suite, unit number, or other address designation.', 
        required=False)
    city = forms.CharField(label='City:', max_length=100)
    state = forms.ChoiceField(choices=models.USState.StatesChoices, label='State') # States model
    
    # Validates 5 numbers, exactly
    zipcode = forms.CharField(label='Zipcode', max_length=5, validators=[RegexValidator(regex='[0-9]{5}')])        


def profile(request):
    if request.method != 'POST':
        form = ProfileForm()
    else: 
        form = ProfileForm(request.POST)
        if form.is_valid():
            return redirect('project:index')
    
    return render(request, 'profile_mgmt/profile_mgmt.html', {'profile_form': form})
