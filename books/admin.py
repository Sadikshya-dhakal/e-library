from django.contrib import admin
from .models import Book
# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_read')  # columns shown in admin list
    list_filter = ('is_read',)
    search_fields = ('title', 'author')

