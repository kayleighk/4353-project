from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
import pytest
import datetime
from django.db.models import ForeignKey
from django.urls import reverse
from users.models import ProfileModel, FuelQuoteModel


# Create your tests here.

#PASSED
@pytest.mark.django_db
def test_user_create():
  User.objects.create_user('john', 'johnpassword')
  assert User.objects.count() == 1

#PASSED
@pytest.mark.django_db
def test_view(client):
   url = reverse('project:index')
   response = client.get(url)
   assert response.status_code == 200

#PASSED
@pytest.mark.django_db
def test_reg_view(client):
   url = reverse('users:register')
   response = client.get(url)
   assert response.status_code == 200

#PASSED
@pytest.mark.django_db
def test_login_view(client):
   url = reverse('users:login')
   response = client.get(url)
   assert response.status_code == 200

#PASSED
@pytest.mark.django_db
def test_login(client):
    User.objects.create_user(username = 'john', password = 'johnpassword')
    c = Client()
    response = c.post('/users/login/', {'username': 'john', 'password': 'johnpassword'})
    assert response.status_code == 302

#PASSED
@pytest.mark.django_db
def test_logout(client):
    c = Client()
    response = c.post('/users/logout/')
    assert response.status_code == 200

#PASSED
@pytest.mark.django_db
def test_incorrect_password(client):
    User.objects.create_user(username = 'john', password = 'johnpassword')
    c = Client()
    response = c.post('/users/login/', {'username': 'john', 'password': 'wrongpassword'})
    assert response.status_code == 200

#PASSED
@pytest.mark.django_db
def test_incorrect_username(client):
    User.objects.create_user(username = 'john', password = 'johnpassword')
    c = Client()
    response = c.post('/users/login/', {'username': 'notjohn', 'password': 'johnpassword'})
    assert response.status_code == 200

#PASSED
@pytest.mark.django_db
def test_register(client):
    c = Client()
    response = c.post('/users/register/', {'username': 'john', 'password': 'johnpassword'})
    assert response.status_code == 200

#PASSED
@pytest.mark.django_db
def test_profile(client):
    User.objects.create_user(username = 'john', password = 'johnpassword')
    c = Client()
    response = c.post('/users/profile/', {'username': 'john', 'password': 'johnpassword'})
    assert response.status_code == 200

#PASSED
@pytest.mark.django_db
def test_fuelquote(client):
    User.objects.create_user(username = 'john', password = 'johnpassword')
    c = Client()
    response = c.post('/users/quoteform/', {'username': 'john', 'password': 'password'})
    assert response.status_code == 200


#PASSED
@pytest.mark.django_db
def test_fuelquote_history(client):
    User.objects.create_user(username = 'john', password = 'johnpassword')
    c = Client()
    response = c.post('/users/quotehistory/', {'username': 'john', 'password': 'password'})
    assert response.status_code == 200


#PASSED
@pytest.mark.django_db
def test_fuelquote_view(client):
    User.objects.create_user(username = 'john', password = 'johnpassword')
    c = Client()

    profile = ProfileModel.objects.create(
        first_name = 'john', 
        last_name = 'smith',
        address_1 = '1234 Test Drive', 
        city = 'Houston', 
        state = 'Texas', 
        zipcode = '12345'
    )

    response = c.post('/users/quoteform/', {'gallons_requested': 10, 'delivery_date': datetime.date.today()})
    assert response.status_code == 200
    


    


#PASSED
@pytest.mark.django_db
def test_profile_info_fields(client):

    User.objects.create_user(username = 'john', password = 'johnpassword')
    c = Client()

    profile = ProfileModel.objects.create(
            first_name = 'john', 
            last_name = 'smith',
            address_1 = '1234 Test Drive', 
            city = 'Houston', 
            state = 'Texas', 
            zipcode = '12345'
        )
    
    assert isinstance(profile.first_name, str)
    assert isinstance(profile.last_name, str)
    assert isinstance(profile.address_1, str)
    assert isinstance(profile.city, str)
    assert isinstance(profile.state, str)
    assert isinstance(profile.zipcode, str)



#PASSED
@pytest.mark.django_db
def test_profile_model(client):

    User.objects.create_user(username = 'john', password = 'johnpassword')
    c = Client()

    profile = ProfileModel.objects.create(
            first_name = 'john', 
            last_name = 'smith',
            address_1 = '1234 Test Drive', 
            city = 'Houston', 
            state = 'Texas', 
            zipcode = '12345'
        )
    

    assert profile.first_name == 'john'
    assert profile.last_name == 'smith'
    assert profile.address_1 == '1234 Test Drive'
    assert profile.city == 'Houston' 
    assert profile.state == 'Texas'
    assert profile.zipcode == '12345'



#PASSED
@pytest.mark.django_db
def test_fuelquote_fields(client):

    user = User.objects.create_user(username = 'john', password = 'johnpassword')
    c = Client()

    quote = FuelQuoteModel.objects.create(
            user = user,
            gallons_requested = 100.0, 
            delivery_date = datetime.date.today(),
            delivery_address = '1234 Test Drive',
            total_amount_due = 100.0
    )
    

    assert isinstance(quote.gallons_requested, float)
    assert isinstance(quote.delivery_date, datetime.date)
    assert isinstance(quote.total_amount_due, float)
    assert isinstance(quote.delivery_address, str)



#PASSED
@pytest.mark.django_db
def test_fuelquote_model(client):

    user = User.objects.create_user(username = 'john', password = 'johnpassword')
    c = Client()

    quote = FuelQuoteModel.objects.create(
            user = user,
            gallons_requested = 100.0, 
            delivery_date = datetime.date.today(),
            delivery_address = '1234 Test Drive',
            total_amount_due = 100.0
        )
    
    assert quote.user == user
    assert quote.gallons_requested == 100.0
    assert quote.delivery_date == datetime.date.today()
    assert quote.total_amount_due == 100.0
    assert quote.delivery_address == '1234 Test Drive'

class FuelTests(TestCase):

    fixtures = ['mydata.json']

    def test_something(self):
        profile=ProfileModel.objects.get(pk=4)
        fuelquotemodel = FuelQuoteModel.objects.get(id=9)

        assert fuelquotemodel.calculate_total_amount_due(profile, True) == 43.5
