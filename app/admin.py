from django.contrib import admin
from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'Mobile','ID','task')  
admin.site.register(User,UserAdmin)


admin.site.register(Task)


