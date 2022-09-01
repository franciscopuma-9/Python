from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField(blank=True,null=True)
    tfno=models.CharField(max_length=7)

class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()

    def __str__(self):
        return 'El nombre es %s la seccion es %s y el precio es %s' % (self.nombre,self.seccion,self.precio)

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()

# __gte = 100  mayor que 100
# __lte = 100  menor que 100
# __range = [50,100] entre 50 y 100
# .order_by('precio') ordena
# .order_by('-precio') ordena al reves