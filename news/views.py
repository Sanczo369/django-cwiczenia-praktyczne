# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.views.generic import ListView
from news.models import News, Category
class IndexView(ListView):
    model = News
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        return News.objects.all().order_by('-id')
class NewsByCategoryView(ListView):
    model = News
    template_name = 'news_by_category.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        category_slug = self.kwargs['slug']
        category = Category.objects.get(slug=category_slug)
        return category.news_set.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = self.kwargs['slug']
        context['c'] = Category.objects.get(slug=category_slug)
        return context