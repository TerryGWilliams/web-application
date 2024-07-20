from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Obituary
from .forms import ObituaryForm

# Create your views here.

def submit_obituary(request):
    if request.method =='POST':
        name = request.POST['name']
        date_of_birth = request.POST['date_of_birth']
        date_of_death = request.POST['date_of_death']
        content = request.POST['content']
        author = request.POST['author']
        slug = generate_unique_slug(name)

        obituary = Obituary(name=name, date_of_birth=date_of_birth, date_of_death=date_of_death, content=content, author=author, slug=slug)
        obituary.save()

        return HttpResponse('Application submitted successfully!')
    
    else:
        return render(request, 'obituary_form.html')




