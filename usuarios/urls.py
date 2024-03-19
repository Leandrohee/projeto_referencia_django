from django.urls import path
from .views import paginaLogin,paginaCadatro

urlpatterns = [
    path('login/', paginaLogin, name='login'),
    path('cadastro/',paginaCadatro, name='cadastro'),
]
