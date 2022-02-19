#URL PATTERNS FOR PROJECT

from django.urls import path

from . import views

app_name = 'project'
urlpatterns = [
    #HOME PAGE
    path('', views.index, name='index'),
]