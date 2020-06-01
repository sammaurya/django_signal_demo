from django.contrib import admin
from .models import UserProfile, Book

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username','first_name','last_name','email','created_by','updated_by')

admin.site.register(UserProfile,UserProfileAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Book,BookAdmin)
