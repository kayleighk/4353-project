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

