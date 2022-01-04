from django.contrib import admin
from .models import *

# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','email','opinion','date_created']

admin.site.register(Comment,CommentAdmin)