from django.shortcuts import render
from .models import Obituary

def view_obituaries(request):
    obituaries = Obituary.objects.all()
    
    return render(request, 'obituaries/view_obituaries.html', {'obituaries': obituaries})
