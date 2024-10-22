from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('title', 'author', 'price', 'status','is_price_high', 'rating', 'rate_with_word',)
    search_fields = ('title', 'author')
    list_filter = ('price','updated_at')
    actions = ['mark_as_published', 'rate_as_5']

    def mark_as_published(self, request, queryset):
        queryset.update(status='published')
        self.message_user(request, "Selected books have been marked as published.")
    mark_as_published.short_description = "Mark selected books as published"
    
    def rate_as_5(self, request, queryset):
        queryset.update(rating=5)
        self.message_user(request, "Selected books have been rated as 5.")
    rate_as_5.short_description = "Rate selected books as 5"
    
    def rate_with_word(self, obj):
        return 'Excellent' if obj.rating == 5 else ('Good' if obj.rating > 2 else 'Bad')
    
    def is_price_high(self, obj):
        return obj.price > 18
    is_price_high.boolean = True
    is_price_high.short_description = 'Price > 18'

admin.site.register(Book, BookAdmin)
