from faulthandler import disable
from unicodedata import decimal
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from users.models import FuelQuoteModel, ProfileModel, USState
from django.core import validators
from django.core.validators import RegexValidator

# Code coverage already exists for this in test.py, already works - Shamee
def register(request): # pragma: no cover
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

# Code coverage already exists for this in test.py, already works - Shamee
def log_in(request): # pragma: no cover
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

# Code coverage already exists for this in test.py, already works - Shamee
def log_out(request): # pragma: no cover
    logout(request)
    return redirect('project:index')


class ProfileForm(forms.ModelForm):

    class Meta:
        model = ProfileModel
        fields = ['first_name', 'last_name', 'address_1', 'address_2','city', 'state', 'zipcode']

    # validate_slug is a Name validation regex, built into Django
    first_name = forms.CharField(label='First name:', max_length=50, validators=[validators.validate_slug], required=True)
    last_name = forms.CharField(label='Last name:', max_length=50, validators=[validators.validate_slug], required=True)

    address_1 = forms.CharField(label='Address:', max_length=100, required=True)
    address_2 = forms.CharField(label='Address 2:', max_length=120,
        help_text='<br/>The apartment, suite, unit number, or other address designation.', 
        required=False)
    city = forms.CharField(label='City:', max_length=100, required=True)
    state = forms.ChoiceField(choices=USState.StatesChoices, label='State', required=True) # States model
    
    # Validates 5 numbers, exactly
    zipcode = forms.CharField(label='Zipcode', max_length=5, validators=[RegexValidator(regex='[0-9]{5}')],required=True)


def profile(request):
    try:
        profile=ProfileModel.objects.get(pk=request.user.id)
    except ProfileModel.DoesNotExist: 
        profile = None
    if request.method != 'POST':
        if profile:
            form = ProfileForm(instance=profile)
        else:
            form = ProfileForm()
    else: 
        form = ProfileForm(request.POST)
        if form.is_valid():

            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()

            return redirect('project:index')
    
    return render(request, 'profile_mgmt/profile_mgmt.html', {'profile_form': form})

class DateInput(forms.widgets.DateInput):
    input_type = 'date'

class FuelQuoteForm(forms.Form):

    gallons_requested = forms.FloatField(label='Gallons requested:', required=True)
    delivery_address = forms.CharField(label='Address:', max_length=100, widget=forms.TextInput(attrs={'readonly':'True'}))
    delivery_date = forms.DateField(widget=DateInput(),label='Delivery date:', required=True)
    suggested_price = forms.FloatField(label='Suggested price/gallon:')
    total_amount_due = forms.FloatField(label='Total amount due:')


def fuelQuoteRequest(request):

    try:
        profile=ProfileModel.objects.get(pk=request.user.id)
    except ProfileModel.DoesNotExist: 
        profile = None

    if profile and profile.address_1:
        if request.method != 'POST':
            form = FuelQuoteForm({'delivery_address': profile.address_1})
        
            return render(request, 'fuel_quote/requestfuelquote.html', {'profileaddress_exists':True,'quoteform': form, 'disablesubmitbutton':True})
        else: 
            # print('get_quote' in request.POST)
            # print(request.POST.get_quote)
            if 'get_quote' in request.POST:
                
                fuelquote = FuelQuoteModel(
                        gallons_requested=request.POST.get('gallons_requested'),
                        delivery_address = profile.address_1,
                        delivery_date = request.POST.get('delivery_date'),                        
                        user = request.user)

                fuelquotehistory = FuelQuoteModel.objects.filter(user_id=request.user.id)

                has_history = (True if fuelquotehistory else False)

                formData = {}
                formData['gallons_requested'] = request.POST.get('gallons_requested')
                formData['delivery_address'] = profile.address_1
                formData['delivery_date'] = request.POST.get('delivery_date')
                formData['suggested_price'] = fuelquote.calculate_suggested_price(profile=profile, has_history=has_history)
                formData['total_amount_due'] = fuelquote.calculate_total_amount_due(profile=profile, has_history=has_history)

                form = FuelQuoteForm(formData)

                return render(request, 'fuel_quote/requestfuelquote.html', {'profileaddress_exists':True,'quoteform': form,'disablesubmitbutton':False})

            elif 'submit_quote' in request.POST:

                fuelquote = FuelQuoteModel(
                        gallons_requested=request.POST.get('gallons_requested'),
                        delivery_address = profile.address_1,
                        delivery_date = request.POST.get('delivery_date'),                        
                        user = request.user)

                fuelquotehistory = FuelQuoteModel.objects.filter(user_id=request.user.id)

                has_history = (True if fuelquotehistory else False)

                formData = {}
                formData['gallons_requested'] = request.POST.get('gallons_requested')
                formData['delivery_address'] = profile.address_1
                formData['delivery_date'] = request.POST.get('delivery_date')
                formData['suggested_price'] = fuelquote.calculate_suggested_price(profile=profile, has_history=has_history)
                formData['total_amount_due'] = fuelquote.calculate_total_amount_due(profile=profile, has_history=has_history)

                form = FuelQuoteForm(formData)

                if form.is_valid():

                    fuelquote = FuelQuoteModel(
                        gallons_requested=form.cleaned_data['gallons_requested'],
                        delivery_address = profile.address_1,
                        delivery_date = form.cleaned_data['delivery_date'],
                        total_amount_due = form.cleaned_data['total_amount_due'],
                        user_id = request.user.id)

                    fuelquote.save()

                    return redirect('project:index')
                

    else:

        return render(request, 'fuel_quote/requestfuelquote.html', {'profileaddress_exists':False})


    # return render(request, 'fuel_quote/requestfuelquote.html', {'fuelquoteform': form})


def fuelQuoteHistory(request):

    fuelquotehistory = FuelQuoteModel.objects.filter(user_id=request.user.id)

    if fuelquotehistory:
        return render(request, 'fuel_quote/fuelquotehistory.html', {'fuelquotehistory_exists':True, 'fuelquotehistory': fuelquotehistory})
    else:
        return render(request, 'fuel_quote/fuelquotehistory.html', {'fuelquotehistory_exists':False})