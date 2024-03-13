from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'recipes/home.html', status=201, context= {
        'name': 'Guilherme'
    })

def contact(request):
    return render(request, 'base.html')

def about(request):
    return HttpResponse('About')