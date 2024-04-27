from django.contrib import admin

# Register your models here.
from .models import Cliente, ClienteProducto, Producto, Transaccion, Tipo_transaccion

admin.site.register(Cliente)
admin.site.register(ClienteProducto)
admin.site.register(Producto)
admin.site.register(Transaccion)
admin.site.register(Tipo_transaccion)