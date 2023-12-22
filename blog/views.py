from django.shortcuts import render
from django.template import RequestContext
def home(request):
    context = {
            'zmienna': 'Jestem widokiem',
            }
    
    return render(request,'home.html',context)