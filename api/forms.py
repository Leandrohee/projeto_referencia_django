#Esse arquivo eh responsavel por configurar os formularios usados para cadastrar um novo pedido
#Depos de configurar os formularios eles sao enviados para o views.py para entao o view mandar eles pro html
#Esse forms sera diferente do forms usado na pasta usuarios, esse nos iremos usar um forms ja "pre programado" do django ao invez de criar um forms do zero igual foi no forms de usuaris

from django import forms                                                                                                #importando o forms do django
from .models import Pedido                                                                                              #vamos importar o models Pedido do DB pois esse nosso formulario sera baseado no modelo do banco de dados

class PedidoForm(forms.ModelForm):                                                                                      #o forms.ModelForm cria um formulario baseando-se em um model do banco de dados
    class Meta:
        model = Pedido                                                                                                  #aqui setamos qual eh o modelo referencia
        fields = ['pedido','oficina','os','os_pdf','prefixo','modelo','data_do_pedido']                                          #colocamos os campos que vao aparecer no formulario
        # exclude = ['usuario_que_add']                                                                                 #ao inves de colocarmos todos os campos que vao aparecer no formularios podemos tb somente excluir os campos que nao queremos que aparece
        labels = {                                                                                                      #no label estamos reescrevendo as labels de cada input para conter letra maiuscula, acentos e espacos
            'pedido': 'Pedido:',                                                                                        #primeiro eh o  nome da variavel depois dois pontos e a string que queremos  que apareca
            'oficina': 'Oficina:',                                                                                      #primeiro eh o  nome da variavel depois dois pontos e a string que queremos  que apareca
            'os': 'O.S:',                                                                                               #primeiro eh o  nome da variavel depois dois pontos e a string que queremos  que apareca
            'os_pdf': 'PDF da O.S:',
            'prefixo': 'Prefixo',                                                                                       #primeiro eh o  nome da variavel depois dois pontos e a string que queremos  que apareca
            'modelo': 'Modelo',                                                                                         #primeiro eh o  nome da variavel depois dois pontos e a string que queremos  que apareca
            'data_do_pedido': 'Data do pedido:'                                                                         #primeiro eh o  nome da variavel depois dois pontos e a string que queremos  que apareca
        }
        widgets={
            'pedido': forms.TextInput(attrs={'class':'input-add'}),                                                     #escolho qual o tipo do input dessae campo no formulario, nesse caso texto. O attrs quer dizer atributo e eh como nos colocamos o nome de uma classe na tag input
            'oficina':forms.Select(attrs={'class':'input-add'}),                                                        #input  tipo selec multiplas opcoes, essas opcoes estao no models.py. O attrs quer dizer atributo e eh como nos colocamos o nome de uma classe na tag input
            'os': forms.TextInput(attrs={'class':'input-add'}),                                                         #O attrs quer dizer atributo e eh como nos colocamos o nome de uma classe na tag input
            'os_pdf': forms.FileInput(attrs={'class':'input-add'}),
            'prefixo': forms.TextInput(attrs={'class':'input-add'}),                                                    #O attrs quer dizer atributo e eh como nos colocamos o nome de uma classe na tag input
            'modelo': forms.TextInput(attrs={'class':'input-add'}),                                                     #O attrs quer dizer atributo e eh como nos colocamos o nome de uma classe na tag input
            'data_do_pedido': forms.DateInput(format= '%d/%m/%Y',attrs={'type':'date','class':'input-add'})             #format  quer dizer o formato da data que queremos inserir
        }

