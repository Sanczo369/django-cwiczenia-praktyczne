from django.urls import path
from . import views
from .views import IndexView, NewsByCategoryView

urlpatterns = [
    path('', IndexView.as_view(), name='IndexView'),
    path('category/<slug:slug>/', NewsByCategoryView.as_view(), name='news_by_category'),
]