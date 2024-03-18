# Eh aqui que vamos crair e configurar os modelos para o banco de dados

from django.db import models
from django.core.validators import MaxValueValidator                        #importando essa classe que limita o numero querido para ate o numero 9999
from datetime import datetime                                               #biblioteca necessaria para adicionar a hora e a data

class Pedido(models.Model):                                                 #Criando uma classe Pedido que contera todos os pedidos criados

    TIPOS_DE_OFICINAS = (                                                   #Criei uma tupla para armazenar as opcoes
        ("Gasolina", "GASOLINA"),
        ("Diesel", "DIESEL"),
        ("Posto", "POSTO"),
        ("Eletrica", "ELETRICA"),
    )

    pedido = models.IntegerField(validators=[MaxValueValidator(9999)],null=False,blank=False)           #o campo pedido so aceitara numeros menores que 9999
    oficina = models.CharField(max_length=15,choices=TIPOS_DE_OFICINAS, blank=False, default='Gas')                           
    os = models.CharField(max_length=10,null=False,blank=False)
    prefixo = models.CharField(max_length=10,null=False,blank=False)
    modelo =  models.CharField(max_length=30,null=False,blank=False)
    data_do_pedido = models.DateTimeField(default=datetime.now, blank = False)                          #add a data que o pedido foi criado

    def __str__(self):
        return (f'Pedido {self.pedido}')