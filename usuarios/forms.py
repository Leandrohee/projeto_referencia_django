#Esse arquivo eh responsavel por configurar os formularios usados para cadastrar um usuario ou autenticar um usuario
#Depos de configurar os formularios eles sao enviados para o views.py para entao o view mandar eles pro html

from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(label="Nome de Login: ", required=True, max_length=50)                                                 #criando label e input do login com esse comando
    senha = forms.CharField(label="Senha: ", required=True, max_length=30, widget= forms.PasswordInput())                               #criando label e input da senha com esse comando

class CadastroForms(forms.Form):
    login_a_cadastrar = forms.CharField(label="Crie um nome de Login: ", required=True, max_length=50)                                  #criando label e input do login a cadastrar com esse comando
    email_a_cadastrar = forms.EmailField(label="Digite seu email: ", required=True, max_length=70, widget=forms.EmailInput())           #criando label e inpput para cadastrar o email
    senha_1 =  forms.CharField(label="Crie uma senha: ", required=True, max_length=30, widget= forms.PasswordInput())                   #criando label e input para cadastrar uma  senha 
    senha_2 =  forms.CharField(label="Confirme sua senha: ", required=True, max_length=30, widget= forms.PasswordInput())               #criando label e input para confirmar uma senha