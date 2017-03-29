# This makes us sends http responses
from django.shortcuts import render


# all views have to accept a request
def homepage(request):
    return render(request, 'home.html')
