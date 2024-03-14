#Esse arquivo eh responsavel por gerenciar as urls que chegam 

from django.urls import path
from .views import renderizandoSimplesHtml, renderizandoUmArquivoHtml

urlpatterns = [
    path('htmlsimples/', renderizandoSimplesHtml),                                           #nessa url relativa sera renderizado um html simples 
    path('',renderizandoUmArquivoHtml)
]