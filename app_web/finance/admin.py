from django.contrib import admin
from .models import Cliente, Producto, ClienteProducto, Tipo_transaccion,Transaccion
# Register your models here.
class ClienteFields(admin.ModelAdmin):
    list_display = ('nombre','apellido','celular','email')
    
class ProductoFields(admin.ModelAdmin):
    list_display = ('nombre_producto','abreviatura','age','ident_number')

admin.site.register(Cliente,ClienteFields)
admin.site.register(Producto, ProductoFields)

