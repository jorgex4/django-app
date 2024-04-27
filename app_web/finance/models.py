from django.db import models
import datetime
from django.contrib.auth.hashers import make_password

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
    contraseña = models.CharField(max_length=250)
    email = models.CharField(max_length=250, null=True, blank=True)
    celular = models.CharField(max_length=250, null=True,blank=True)
    
    def save(self, *args, **kwargs):
        self.contraseña = make_password(self.contraseña) 
        super().save(*args, **kwargs)


    def __str__(self):
        return self.nombre + ' ' + self.apellido + ' - ' + self.celular + ' - ' + self.email
    
    
class Producto(DateTimeModel):
    nombre_producto = models.CharField(max_length=100, blank=True)
    abreviatura = models.CharField(max_length=100, blank=True)
    descripcion = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.nombre_producto + ' (' + self.abreviatura + ')' + ' - ' + self.descripcion
    
class ClienteProducto(DateTimeModel):
    
   id_cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)
   id_producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
   numero_cuenta=models.CharField(max_length=50)
   def __str__(self):
        return self.id_cliente.nombre + ' ' + self.id_cliente.apellido + ' - ' + self.id_producto.nombre_producto
   

class Tipo_transaccion(DateTimeModel):
    nombre = models.CharField(max_length=100, blank=True)
    abreviatura = models.CharField(max_length=100, blank=True)
    descripcion = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.nombre + ' (' + self.abreviatura + ')' + ' - ' + self.descripcion
    
class Transaccion(DateTimeModel):
    id_cliente_producto = models.ForeignKey(ClienteProducto, on_delete=models.CASCADE)
    id_tipo_transaccion = models.ForeignKey(Tipo_transaccion, on_delete=models.CASCADE)
    monto = models.CharField()
    Tipo_transaccion = models.CharField(max_length=100, blank=True)