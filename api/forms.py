#Esse arquivo eh responsavel por configurar os formularios usados para cadastrar um novo pedido
#Depos de configurar os formularios eles sao enviados para o views.py para entao o view mandar eles pro html
#Esse forms sera diferente do forms usado na pasta usuarios, esse nos iremos usar um forms ja "pre programado" do django ao invez de criar um forms do zero igual foi no forms de usuaris

from django import forms                                                                                                #importando o forms do django
from .models import Pedido                                                                                              #vamos importar o models Pedido do DB pois esse nosso formulario sera baseado no modelo do banco de dados

class PedidoForm(forms.ModelForm):                                                                                      #o forms.ModelForm cria um formulario baseando-se em um model do banco de dados
    class Meta:
        model = Pedido                                                                                                  #aqui setamos qual eh o modelo referencia
        fields = ['pedido','oficina','os','prefixo','modelo','data_do_pedido']                                          #colocamos os campos que vao aparecer no formulario
        # exclude = ['usuario_que_add']                                                                                 #ao inves de colocarmos todos os campos que vao aparecer no formularios podemos tb somente excluir os campos que nao queremos que aparece
        widgets={
            'pedido': forms.TextInput(attrs={'class':'input-add'}),
            'oficina':forms.Select(attrs={'class':'input-add'}),
            'os': forms.TextInput(attrs={'class':'input-add'}),
            'prefixo': forms.TextInput(attrs={'class':'input-add'}),
            'modelo': forms.TextInput(attrs={'class':'input-add'}),
            'data_do_pedido': forms.DateInput(format= '%d/%m/%Y',attrs={'type':'date','class':'input-add'})
        }

