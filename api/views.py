#Eh nesse arquivo que sao enviadas as informacoes para renderizacao seja em html, texto simples, json ou qualquer outra funcao

from django.shortcuts import render,redirect                                                #Consigo pegar um model do Db com essa funcao
from django.http import HttpResponse                                                        #importei essa classe que eh responsavel por renderizar um html puro
from django.contrib import messages                                                          #importando mensagens de aviso para ser utilizadas nos formularios do html
from .models import Pedido
from .forms import PedidoForm

def renderizandoSimplesHtml(request):                                                       #fiz uma funcao que ira retornar um texto simples com html puro 
    return HttpResponse('<h1>Deu certo!!</h1><p>Aqui esta um html simples</p>')

def renderizandoUmArquivoHtml(request):                                                     #fiz uma funcao que ira renderizar um arquivo .html ***EH O PRINCIPAL DO PROJETO***
    if not request.user.is_authenticated:                                                   # verifica se o usuario esta logado
        messages.error(request, "Faca o login")                                             #mensagem de aviso para fazer login         
        return redirect('login')                                                            #se nao  estiver logado redireciona para a pagina de login

    pedidos_do_db = Pedido.objects.all()                                                    #pegando todos os dados do modelo Pedido e envia paraa a variavel pedidos_do_db
    pedidos_organizados = Pedido.objects.order_by("pedido")                                 #filtrando os pedidos do banco de dados por numero do pedido
    return render(request, 'principal/index.html',{"pedidos_enviados": pedidos_organizados})    #para ele conseguer ler o arquivo index.html o caminho da pasta dele deve ser configurada no settings.py na aba DIRS
    

def renderizandoPedidosIndividuais(request,pedido_id):                                          #Esse parametro "pedido_id" tem que coincidir com o nome no url.py no path de renderizandoPedidosIndividuais
    pedido_clicado = Pedido.objects.filter(id=pedido_id).get()                                  #filtrei para condizer com o id do pedido clicado em index.html. o id foi enviado pelo index.html para a url que passou o parametro para essa funcao em pedido_id
    return render(request,'principal/pedido.html',{"pedidos_enviados": pedido_clicado})

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

def addNovoPedido(request):
    form = PedidoForm()
    return render(request, 'principal/adicionar-pedido.html', {"form": form})

def editandoPedido(request):
    pass

def deletandoPedido(request):
    pass