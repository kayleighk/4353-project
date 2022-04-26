from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class USState(models.Model):
    Alabama = 'AL'
    Alaska = 'AK'
    Arizona = 'AZ'
    Arkansas = 'AR'
    California = 'CA'
    Colorado = 'CO'
    Connecticut = 'CT'
    Delaware = 'DE'
    Florida = 'FL'
    Georgia = 'GA'
    Hawaii = 'HI'
    Idaho = 'ID'
    Illinois = 'IL' 
    Indiana = 'IN'
    Iowa = 'IA'
    Kansas = 'KS'
    Kentucky = 'KY'
    Louisiana = 'LA'
    Maine = 'ME'
    Maryland = 'MD' 
    Massachusetts = 'MA' 
    Michigan = 'MI'
    Minnesota = 'MN'
    Mississippi = 'MS'
    Missouri = 'MO'
    Montana = 'MT'
    Nebraska = 'NE'
    Nevada = 'NV'
    NewHampshire = 'NH' 
    NewJersey = 'NJ'
    NewMexico = 'NM'
    NewYork = 'NY'
    NorthCarolina = 'NC' 
    NorthDakota = 'ND'
    Ohio = 'OH'
    Oklahoma = 'OK' 
    Oregon = 'OR'
    Pennsylvania = 'PA' 
    RhodeIsland = 'RI'
    SouthCarolina = 'SC'
    SouthDakota = 'SD'
    Tennessee = 'TN'
    Texas = 'TX'
    Utah = 'UT'
    Vermont = 'VT'
    Virginia = 'VA'
    Washington = 'WA'
    WestVirginia = 'WV'
    Wisconsin = 'WI'
    Wyoming = 'WY'

    StatesChoices = [
        (Alabama, "Alabama"),
        (Alaska, "Alaska"),
        (Arizona, "Arizona"),
        (Arkansas, "Arkansas"),
        (California, "California"),
        (Colorado, "Colorado"),
        (Connecticut, "Connecticut"),
        (Delaware, "Delaware"),
        (Florida, "Florida"),
        (Georgia, "Georgia"),
        (Hawaii, "Hawaii" ),
        (Idaho, "Idaho"),
        (Illinois, "Illinois"),
        (Indiana, "Indiana" ),
        (Iowa, "Iowa"),
        (Kansas, "Kansas"),
        (Kentucky, "Kentucky"),
        (Louisiana, "Louisiana"),
        (Maine, "Maine"),
        (Maryland, "Maryland"),
        (Massachusetts, "Massachusetts"),
        (Michigan, "Michigan"),
        (Minnesota, "Minnesota"),
        (Mississippi, "Mississippi"),
        (Missouri, "Missouri"),
        (Montana, "Montana"),
        (Nebraska, "Nebraska"),
        (Nevada, "Nevada"),
        (NewHampshire, "New Hampshire"),
        (NewJersey, "New Jersey"),
        (NewMexico, "New Mexico"),
        (NewYork, "New York"),
        (NorthCarolina, "North Carolina"),
        (NorthDakota, "North Dakota"),
        (Ohio, "Ohio"),
        (Oklahoma, "Oklahoma"),
        (Oregon, "Oregon"),
        (Pennsylvania, "Pennsylvania"),
        (RhodeIsland, "Rhode Island"),
        (SouthCarolina, "South Carolina"),
        (SouthDakota, "South Dakota"),
        (Tennessee, "Tennessee"),
        (Texas, "Texas"),
        (Utah, "Utah"),
        (Vermont, "Vermont"),
        (Virginia, "Virginia"),
        (Washington, "Washington"),
        (WestVirginia, "West Virginia"),
        (Wisconsin, "Wisconsin"),
        (Wyoming, "Wyoming"),
    ]

class ProfileModel(models.Model):
    
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    # validate_slug is a Name validation regex, built into Django
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=120,blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100,choices=USState.StatesChoices) # States model
    
    # Validates 5 numbers, exactly
    zipcode = models.CharField(max_length=5) 

class FuelQuoteModel(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    # profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)

    gallons_requested = models.FloatField()
    delivery_address = models.CharField(max_length=100)
    # delivery_address_2 = models.CharField(max_length=100,blank=True)
    delivery_date = models.DateField(blank=True)
    total_amount_due = models.FloatField()

    # @property
    def calculate_suggested_price(self,profile,has_history):
        
        # Location Factor = 2% for Texas, 4% for out of state.
        location_factor = (0.02 if profile.state=="TX" else 0.04)

        # Rate History Factor = 1% if client requested fuel before, 0% if no history (you can query fuel quote table to check if there are any rows for the client)
        
        rate_history_factor = (0.01 if has_history else 0.00)

        # Gallons Requested Factor = 2% if more than 1000 Gallons, 3% if less
        gallons_requested_factor = (0.02 if float(self.gallons_requested) > 1000 else 0.03)

        # Company Profit Factor = 10% always
        company_profit_factor = 0.10

        # Current price per gallon = $1.50 (this is the price what distributor gets from refinery and it varies based upon crude price. But we are keeping it constant for simplicity)
        currentprice = 1.50

        margin = currentprice * (location_factor - rate_history_factor + gallons_requested_factor + company_profit_factor)

        suggested_price = margin + currentprice
        return suggested_price

    # Get Quote
    @property
    def calculate_total_amount_due(self):
        return self.gallons_requested * self.calculate_suggested_price(self)
    # @property
    def calculate_total_amount_due(self, profile, has_history):
        return float(self.gallons_requested) * self.calculate_suggested_price(profile, has_history)
