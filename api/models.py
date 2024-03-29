# Eh aqui que vamos crair e configurar os modelos para o banco de dados

from django.db import models
from django.core.validators import MaxValueValidator                                                            #importando essa classe que limita o numero querido para ate o numero 9999
from datetime import datetime                                                                                   #biblioteca necessaria para adicionar a hora e a data
from django.contrib.auth.models import User                                                                     #importando o modelo User nativo do Django que armazena todos os usuarios
from django.core.exceptions import ValidationError                                                              #Iportando uma mensagem de error            

def validandoPdf(valor):                                                                                        #Essa funcao vai validar se o arquivo  que fiz upload eh no formato pdf
    if not valor.name.lower().endswith('.pdf'):                                                                 #coloca o nome do arquivo em letra minuscla e verifica se o final do arquivo eh pdf    
        raise ValidationError(('O arquivo deve estar em formato PDF!'))

class Pedido(models.Model):                                                                                     #Criando uma classe Pedido que contera todos os pedidos criados

    TIPOS_DE_OFICINAS = (                                                                                       #Criei uma tupla para armazenar as opcoes
        ("Gasolina", "GASOLINA"),
        ("Diesel", "DIESEL"),
        ("Posto", "POSTO"),
        ("Eletrica", "ELETRICA"),
    )

    pedido = models.IntegerField(validators=[MaxValueValidator(9999)],null=False,blank=False)                   #o campo pedido so aceitara numeros menores que 9999
    oficina = models.CharField(max_length=15,choices=TIPOS_DE_OFICINAS, blank=False, default='Gas')                           
    os = models.CharField(max_length=10,null=False,blank=False)
    os_pdf = models.FileField(validators=[validandoPdf], null=False, blank=True, default='')
    prefixo = models.CharField(max_length=10,null=False,blank=False)
    modelo =  models.CharField(max_length=30,null=False,blank=False)
    data_do_pedido = models.DateTimeField(default=datetime.now, blank = False)                                  #add a data que o pedido foi criado
    usuario_que_add = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=False, related_name='usuarioadd')

    def __str__(self):
        return (f'Pedido {self.pedido}')