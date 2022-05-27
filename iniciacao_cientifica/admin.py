from django.contrib import admin
from .models import *

class AutorAdmin(admin.ModelAdmin):
    list_display = ['name']

class UserAdmin(admin.ModelAdmin):
    def timestamp(self):
        time = self.time.strftime('%a %H:%M  %d/%m/%y')
        return time
    list_display = ['name', 'username', 'institution', 'get_articles', 'areasofinterest', 'timestamp']

    

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_authors', 'abstract', 'event', 'pub_date']


admin.site.register(Author, AutorAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Article, ArticleAdmin)
