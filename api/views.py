#Eh nesse arquivo que sao enviadas as informacoes para renderizacao seja em html, texto simples, json ou qualquer outra funcao

from django.shortcuts import render
from django.http import HttpResponse                                                        #importei essa classe que eh responsavel por renderizar um html puro

def renderizandoSimplesHtml(request):                                                       #fiz uma funcao que ira retornar um texto simples com html puro 
    return HttpResponse('<h1>Deu certo!!</h1><p>Aqui esta um html simples</p>')

def renderizandoUmArquivoHtml(request):                                                     #fiz uma funcao que ira renderizar um arquivo .html
    return render(request, 'principal/index.html')                                                    #para ele conseguer ler o arquivo index.html o caminho da pasta dele deve ser configurada no settings.py na aba DIRS