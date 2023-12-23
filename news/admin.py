from django.contrib import admin

# Register your models here.
from news.models import Category, News
# dla kategorii
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','icon')
    prepopulated_fields = {'slug': ('name',)}
    
# dla wiadomości
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','date')
    prepopulated_fields = {'slug': ('title',)}
    search_fields =  ['title', 'text']
    date_hierarchy = "date"

    
# rejestracja wraz z podaniem klasy konfigurującej PA
admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)