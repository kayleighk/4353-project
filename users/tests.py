from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
import pytest
from django.urls import reverse


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
    response = c.post('/users/login/', {'username': 'notjohn', 'password': 'password'})
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
    response = c.post('/users/profile/', {'username': 'notjohn', 'password': 'password'})
    assert response.status_code == 200