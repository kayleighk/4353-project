from django.shortcuts import render

def index(request):
    #PROJECT HOME PAGE
    return render(request, 'project/index.html')
