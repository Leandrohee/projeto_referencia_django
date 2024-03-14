from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls'))                                       #aqui estou enviando a url vazia para o app api para que ele faça o gerenciamento dessa url vazia
]
