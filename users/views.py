from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

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