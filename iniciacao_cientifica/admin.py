from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'username', 'institution', 'areasofinterest', 'timestamp']

admin.site.register(User, UserAdmin)
admin.site.register(Article)
