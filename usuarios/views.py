from django.shortcuts import render
from .forms import LoginForms, CadastroForms

def paginaLogin(request):
    form = LoginForms()                                                         #instanciando a variavel form com a classe LoginForms criada no forms.py
    return render(request, 'login/login.html', {"form": form})                  #enviando o form criado para o html

def paginaCadatro(request):
    form = CadastroForms()                                                      #instanciando a variavel form com a classe CadastroForms criada no forms.py     
    return render(request, 'login/cadastro.html', {"form": form})               #enviando o form criado para o html     