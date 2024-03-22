#Esse arquivo eh responsavel por gerenciar as urls que chegam 

from django.urls import path
from .views import renderizandoUmArquivoHtml,renderizandoPedidosIndividuais
from .views import renderizandoSimplesHtml, enviandoDadosSemDB, renderizandoPaginaBuscar
from .views import addNovoPedido, deletarPedido, editarPedido 

urlpatterns = [
    path('htmlsimples/', renderizandoSimplesHtml),                                                  #nessa url relativa sera renderizado um html simples 
    path('enviandodadossemdb/',enviandoDadosSemDB),                                                 #essa url eh para exibir um envio de dados sem a necessidade de banco de dados 
    path('',renderizandoUmArquivoHtml,name='principal'),                                            #path para o html principal
    path('pedido/<int:pedido_id>',renderizandoPedidosIndividuais, name='pedido'),                   #o <int:pedido_id> quer dizer que o numero na URL depois de "pedido/"" sera salvo na variavel "pedido_id" essa variavel sera enviada como parametro para a funcao renderizandoPedidosIndividuais em views.py
    path('buscar/',renderizandoPaginaBuscar, name='buscar'),                                        #path para o html da pagina de buscas
    path('addNovoPedido/',addNovoPedido, name='addNovoPedido'),
    path('editarPedido/<int:pedido_id>',editarPedido, name='editarPedido'),                         #o <int:pedido_id> quer dizer que o numero na URL depois de "editarPedido/" sera salvo na variavel "pedido_id" essa variavel sera enviada como parametro para a funcao editarPedido em views.py
]