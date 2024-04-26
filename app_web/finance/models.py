from django.db import models
import datetime

#model.DateTimeField(auto_now=True, null=False) => updated_at
#model.DateTimeField(auto_now_at=True, null=False) => Default now()

# Create your models here.
class DateTimeModel(models.Model):
     updated_at = models.DateTimeField(default=datetime.datetime.now ())
     created_at = models.DateTimeField(default=datetime.datetime.now ())
     deleted_at = models.DateTimeField(null=True, blank=True)
     class Meta:
         abstract = True
         
class Cliente(DateTimeModel):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    celular = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    
    
class Producto(DateTimeModel):
    nombre_producto = models.CharField(max_length=100, blank=True)
    abreviatura = models.CharField(max_length=10, blank=True)
    descripcion = models.CharField(max_length=10, blank=True)
    
class ClienteProducto(DateTimeModel):
   id_cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE, blank = False, null=False, default=1)
   id_producto=models.ForeignKey(Producto, on_delete=models.CASCADE, blank = False, null=False, default=1)
   numero_cuenta=models.IntegerField(null=True, blank=True)
   

class Tipo_transaccion(DateTimeModel):
    nombre = models.CharField(max_length=100, blank=True)
    abreviatura = models.CharField(max_length=10, blank=True)
    descripcion = models.CharField(max_length=10, blank=True)
    
class Transaccion(DateTimeModel):
    id_cliente_producto = models.ForeignKey(ClienteProducto, on_delete=models.CASCADE, blank = False, null=False, default=1)
    monto = models.IntegerField()
    Tipo_transaccion = models.CharField(null=True, blank=True, default = True)