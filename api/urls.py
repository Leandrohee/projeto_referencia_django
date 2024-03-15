#Esse arquivo eh responsavel por gerenciar as urls que chegam 

from django.urls import path
from .views import renderizandoSimplesHtml, renderizandoUmArquivoHtml,renderizandoPedidosIndividuais

urlpatterns = [
    path('htmlsimples/', renderizandoSimplesHtml),                                              #nessa url relativa sera renderizado um html simples 
    path('',renderizandoUmArquivoHtml,),                                                        #path para o html principal
    path('pedido/',renderizandoPedidosIndividuais, name='pedido')                               #path para o html de um pedido especifico, esse name eh importante
]