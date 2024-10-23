from django.contrib import admin
from .models import Vehiculo

class VehiculoAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    list_display = ('marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio')
    search_fields = ('serial_carroceria', 'serial_motor')
    list_filter = ('categoria',)

admin.site.register(Vehiculo, VehiculoAdmin)