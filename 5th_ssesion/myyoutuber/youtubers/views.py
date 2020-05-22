from django.shortcuts import render
from .models import youtubers

def home(request):
    likelion = youtubers.objects
    return render(request, 'home.html',{'youtuber':likelion})



# Create your views here.
