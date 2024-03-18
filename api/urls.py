#Esse arquivo eh responsavel por gerenciar as urls que chegam 

from django.urls import path
from .views import renderizandoUmArquivoHtml,renderizandoPedidosIndividuais
from .views import renderizandoSimplesHtml, enviandoDadosSemDB, renderizandoPaginaBuscar 

urlpatterns = [
    path('htmlsimples/', renderizandoSimplesHtml),                                              #nessa url relativa sera renderizado um html simples 
    path('enviandodadossemdb/',enviandoDadosSemDB),                                             #essa url eh para exibir um envio de dados sem a necessidade de banco de dados 
    path('',renderizandoUmArquivoHtml,name='principal'),                                        #path para o html principal
    path('pedido/<int:pedido_id>',renderizandoPedidosIndividuais, name='pedido'),                #path para o html de um pedido especifico, esse name eh importante
    path('buscar/',renderizandoPaginaBuscar, name='buscar')                                     #path para o html da pagina de buscas
]