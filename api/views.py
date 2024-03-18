#Eh nesse arquivo que sao enviadas as informacoes para renderizacao seja em html, texto simples, json ou qualquer outra funcao

from django.shortcuts import render                                                         #Consigo pegar um model do Db com essa funcao
from django.http import HttpResponse                                                        #importei essa classe que eh responsavel por renderizar um html puro
from .models import Pedido

def renderizandoSimplesHtml(request):                                                       #fiz uma funcao que ira retornar um texto simples com html puro 
    return HttpResponse('<h1>Deu certo!!</h1><p>Aqui esta um html simples</p>')

def renderizandoUmArquivoHtml(request):                                                     #fiz uma funcao que ira renderizar um arquivo .html ***EH O PRINCIPAL DO PROJETO***
    pedidos_do_db = Pedido.objects.all()                                                    #pegando todos os dados do modelo Pedido e envia paraa a variavel pedidos_do_db
    pedidos_organizados = Pedido.objects.order_by("pedido")                                 #filtrando os pedidos do banco de dados por numero do pedido
    return render(request, 'principal/index.html',{"pedidos_enviados": pedidos_organizados})    #para ele conseguer ler o arquivo index.html o caminho da pasta dele deve ser configurada no settings.py na aba DIRS

def renderizandoPedidosIndividuais(request):                                                #renderiza o html referente a um pedido
    return render(request,'principal/pedido.html')

def renderizandoPaginaBuscar(request):                                                      #criei uma funcao que mostrara itens filtrados
    pedidos_organizados = Pedido.objects.order_by("pedido")                                 #filtrando os pedidos do banco de dados por numero do pedido

    if "input-buscar" in request.GET:                                                           #se a string "input-buscar" estiver na url (requst.get puxa a url) prossiga
        pedido_a_buscar = request.GET['input-buscar']                                           #coloca o que vem depois da string 'input-buscar' na url na variavel pedido_a_buscar
        if pedido_a_buscar:                                                                     #se a variavel pedido_a_buscar nao estiver vazia, ou seja o campo buscar em branco prosseguir
            pedidos_filtrados = pedidos_organizados.filter(pedido__icontains=pedido_a_buscar)   #__icontains eh uma funcao do django que procura o texto desejado no campo pedido em todos os elementos do modelo Pedido 

    return render(request, 'principal/buscar.html', {"pedidos_enviados": pedidos_filtrados})    #renderiza a pagina buscar.html e envia para ela a lista dos pedidos filtrados pelo numero do pedido    

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
