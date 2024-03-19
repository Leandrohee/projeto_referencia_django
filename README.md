-->  A pasta api eh responsavel pelo layout principal assim como o modelos Pedido do baco de dados

--> A pasta frontend eh onde ficam todos  os htmls e css do projeto

--> A pasta projeto_referencia.. eh referente a pasta principal do  projeto,  a pasta settings fica aqui

--> A pasta usuarios eh responsavel pelo gerenciamento de usuarios,  login, cadastro e autenticacoes


Geralmetne a logica dos arquivos em um projeto django eh da seguinte forma

** urls.py(setup|projeto) --> urls.py(app) --> views.py(app) --> pagina.html

** models.py --> views.py(app) --> pagina.html