# Nesse arquivo é onde configuramos os dados que seráo gerenciados e exibidos na página de administrador

from django.contrib import admin
from .models import Pedido


class Pedidos(admin.ModelAdmin):                                            #Criei uma classe para gerenciar o models Pedido na url do admin 
    list_display = ("pedido","oficina","os","prefixo","modelo")             #Escolhendo quais parametros do modelo Pedido eu quero gerenciar pelo adm
    list_display_links = ("pedido",)                                        #Qual parametro eu quero poder ter acesos para clicar
    search_fields = ("pedido",)                                             #Quero pesquisar por qual parametro
    list_filter = ("oficina", "modelo", "prefixo")                          #Criando filtros para visualizar no adm
    list_per_page = 1000                                                    #Quantos itens por pagina

admin.site.register(Pedido,Pedidos)                                         #Com esse comando eu subo esssa classe Pedidos para a ulr admin