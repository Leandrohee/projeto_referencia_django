from django.shortcuts import render
from django.http import HttpResponse

def paginaLogin(request):                                                       
    return render(request, 'login/login.html')

def paginaCadatro(request):                                                       
    return render(request, 'login/cadastro.html')