from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto

class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('pk','nombre')
admin.site.register(Laboratorio, LaboratorioAdmin)

class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('pk','nombre','laboratorio')
admin.site.register(DirectorGeneral, DirectorGeneralAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('pk','nombre','laboratorio','f_fabricacion','p_costo','p_venta')
admin.site.register(Producto, ProductoAdmin)
