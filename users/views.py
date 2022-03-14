from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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