from django.shortcuts import render, redirect
from .forms import LoginForms, CadastroForms
from django.contrib.auth.models import User                                                                     #importando o modelo User nativo do Django que armazena todos os usuarios
from django.contrib import auth                                                                                 #esse auth eh para autenticar um usuario
from django.contrib import messages                                                                             #importando mensagens de aviso para ser utilizadas nos formularios do html

def paginaLogin(request):

    if request.method == 'POST':
        form_preenchido = LoginForms(request.POST)                                                              #pega o formulario preenchido no login e coloca na variavel form_preenchido

        if form_preenchido.is_valid():                                                                          #se todos os dados do form estiverem validos seguir
            nome_preenchido = form_preenchido['nome_login'].value()                                             
            senha_preenchida = form_preenchido['senha'].value()

            usuario_preenchido = auth.authenticate(                                                             #autenticando se os dados preenchidos com o form correspodem a algum modelo no banco de dados
                request, 
                username=nome_preenchido,                                                                       #autenticando o nome 
                password=senha_preenchida                                                                       #autenticando a senha
            )

            if usuario_preenchido is not None:                                                                  #se o usuario preenchido nao for vazio eh sinal que o usuario ja encontrase cadstro portando fazer login
                auth.login(request,usuario_preenchido)                                                          #fazer login
                messages.success(request, "Usuario logado com sucesso")                                         #mensagem de aviso. tem que modificar o html para receber essa mensagem
                return redirect('principal')                                                                    #esse redirect faz referencia ao name setado nos arquivos urls.py
            else:
                messages.error(request,"Usuario ou senha incorretos")                                                   #mensagem de erro. tem que modificar o html para receber essa mensagem
                return redirect('login')                                                                        #esse redirect faz referencia ao name setado nos arquivos urls.py

    if request.method == 'GET':                                                                                 #esse request.method = 'get' eh desnecessario pq ele ja eh automatico na funcao get mas coloquei pra ficar mais legivel o codigo ja que tem uma funcao post la em cima
        form = LoginForms()                                                                                     #instanciando a variavel form com a classe LoginForms criada no forms.py
        return render(request, 'login/login.html', {"form": form})                                              #enviando o form criado para o html

def paginaCadatro(request):
    
    if request.method == 'POST':                                                                                #se o metodo de envio for post fazer o seguinte. esse metodo post eh setado no form do html 
        form_preenchido = CadastroForms(request.POST)                                                           #pega todos os dados preenchidos no formulario do html e passa para a variavel form_preenchido       
    
        if form_preenchido.is_valid():                                                                          #se todos os campos preenchidos do formulario no cadastro.html forem validos seguir
            if form_preenchido['senha_1'].value() != form_preenchido['senha_2'].value():                        #se a senha 1 nao for a senha 2 recarregar a pagina. ESSA VALIDACAO PODE SER FEITA TB NO PROPRIO FORMS.PY MAS DEIXEI UMA VALIDACAO AQUI SOMENTE PARA EU SABER 2 FORMAS DE VALIDAR DADOS DE UM  FORMS
                messages.error(request,"as senhas nao sao iguais")                                              #mensagem de aviso. tem que modificar o html para receber essa mensagem
                return redirect('cadastro')                                                                     #recarrega a pagina se as senhas nao forem iguais

            nome_preenchido = form_preenchido['login_a_cadastrar'].value()                                      #esse nome entre aspas eh setado na hora de criar a classe CadastroForms em forms.py 
            email_preenchido = form_preenchido['email_a_cadastrar'].value()                                     #coloquei o email preenchido no formulario do html nessa variavel
            senha_preenchida = form_preenchido['senha_1'].value()                                               #coloquei a senha preenchida no formulario do html nessa variavel

            if User.objects.filter(username=nome_preenchido).exists():                                          #se o nome|login preenchido no forms do html ja estiver em uso por algum usuario no DB recarregar a pagina cadastro
                messages.error(request, "usuario ja cadastrado")                                                #mensagem de aviso. tem que modificar o html para receber essa mensagem
                return redirect('cadastro')                                                                     #Recarrega a pagina caso nome de login duplicado

            novo_usuario = User.objects.create_user(                                                            #criando um novo usuario
                username=nome_preenchido,
                email=email_preenchido,
                password=senha_preenchida
            )
            novo_usuario.save()                                                                                 #salvando o novo usuario do banco de dados

            messages.success(request, "Usuario criado com sucesso")                                             #mensagem de aviso. tem que modificar o html para receber essa mensagem
            return redirect('login')                                                                            #depois de salvo o usuario direcionar para a área de login. esse redirect faz referencia ao name setado nos arquivos urls.py

    if request.method == 'GET':                                                                                 #esse request.method = 'get' eh desnecessario pq ele ja eh automatico na funcao get mas coloquei pra ficar mais legivel o codigo ja que tem uma funcao post la em cima
        form = CadastroForms()                                                                                  #instanciando a variavel form com a classe CadastroForms criada no forms.py     

        return render(request, 'login/cadastro.html', {"form": form})                                           #enviando o form criado para o html     
    
def logout(request):
    auth.logout(request)                                                                                        #comando para logar o usuario logado
    messages.success(request, 'Usuario deslogado com sucesso')
    return redirect('login') 