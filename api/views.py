#Eh nesse arquivo que sao enviadas as informacoes para renderizacao seja em html, texto simples, json ou qualquer outra funcao

from django.shortcuts import render                                                         #Consigo pegar um model do Db com essa funcao
from django.http import HttpResponse                                                        #importei essa classe que eh responsavel por renderizar um html puro
from .models import Pedido

def renderizandoSimplesHtml(request):                                                       #fiz uma funcao que ira retornar um texto simples com html puro 
    return HttpResponse('<h1>Deu certo!!</h1><p>Aqui esta um html simples</p>')

def renderizandoUmArquivoHtml(request):                                                     #fiz uma funcao que ira renderizar um arquivo .html ***EH O PRINCIPAL DO PROJETO***
    pedidos_do_db = Pedido.objects.all()                                                    #pegando todos os dados do modelo Pedido e envia paraa a variavel pedidos_do_db
    pedidos_filtrados = Pedido.objects.order_by("pedido")                                   #filtrando os pedidos do banco de dados por numero do pedido
    return render(request, 'principal/index.html',{"pedidos_enviados": pedidos_filtrados})  #para ele conseguer ler o arquivo index.html o caminho da pasta dele deve ser configurada no settings.py na aba DIRS

def renderizandoPedidosIndividuais(request):                                                #renderiza o html referente a um pedido
    return render(request,'principal/pedido.html')

def enviandoDadosSemDB(request):                                                            #essa funcao de renderizao eh somente para simular o envio de dados sem a ncessidade de um banco de dados
    dados={                                                                                 #criei um dicionario contendo 3 dicionarios dentro para fazer o  envio  dos dados para o html
        1:{
            "nome": "leandro",
            "idade": 29
        },
        2:{
            "nome": "rafael",
            "idade": 27
        },
        3:{
             "nome": "felipe",
            "idade": 18
        }
    }
    
    return render(request, 'principal/htmlsemdb.html', {"dados_enviados": dados} )           #o terceiro parametro eh referente ao dado que eu quero enviar para o html, no caso  estou enviando um dicionario aninhado
