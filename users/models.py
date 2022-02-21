from django.db import models

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
