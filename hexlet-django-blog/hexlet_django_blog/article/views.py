from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Articles',
        'description': 'This is the articles index page.',
    }
    return render(request, 'articles/index.html', context)