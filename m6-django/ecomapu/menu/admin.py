from django.contrib import admin
from menu.models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'category', 'image']
    search_fields = ['name']
admin.site.register(MenuItem, MenuItemAdmin)