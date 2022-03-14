#URL PATTERNS FOR USERS

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    #INCLUDE DEFAULT AUTH URLS
    path('', include('django.contrib.auth.urls')),
    #REGISTRATION PAGE
    path('register/', views.register, name='register'),
<<<<<<< HEAD
    #LOGIN PAGE
    path('login/', views.log_in, name='login'),
    #LOGOUT PAGE
    path('logout/', views.log_out, name='logout'),
=======
    path('profile/', views.profile, name='profilemgmt')
>>>>>>> 72562e9898e1bbe97ba5a0753a859ab33e400d62
]