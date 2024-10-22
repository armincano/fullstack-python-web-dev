from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('title', 'author', 'price')
    search_fields = ('title', 'author')
    list_filter = ('price','updated_at')

admin.site.register(Book, BookAdmin)
