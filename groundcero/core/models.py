from django.db import models
from django.db.models.fields import CharField

class Pedido(models.Model):
    RutCliente=models.CharField(max_length=10,primary_key=True,verbose_name='RutCliente')
    #Nombre=models.CharField(max_length=70,verbose_name='Nombre')
    Joyas=models.CharField(max_length=25,verbose_name='Joyas')
    Dirección=models.CharField(max_length=40,verbose_name='Dirección')
    def __str__(self):
        return(self.RutCliente)

