from django.shortcuts import render
from .models import News
# Create your views here.
def news(request):
    news = News.objects.all().order_by('-id')
    context = {
        'news': news,
        }
    return render(request,'index.html',context)