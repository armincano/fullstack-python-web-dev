from django.contrib import admin
from .models import Producto, Fabricante

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'fabricante', 'f_vencimiento_year')
    list_filter = ('fabricante', 'f_vencimiento')
    search_fields = ('nombre', 'descripcion')
    date_hierarchy = 'f_vencimiento'
    
    def f_vencimiento_year(self, obj):
        return obj.f_vencimiento.year if obj.f_vencimiento else None
    f_vencimiento_year.short_description = 'Año de Vencimiento'
    
admin.site.register(Producto, ProductoAdmin)

class FabricanteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais')
    search_fields = ('nombre', 'pais')

admin.site.register(Fabricante, FabricanteAdmin)