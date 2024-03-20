from django.urls import path
from .views import paginaLogin,paginaCadatro,logout

urlpatterns = [
    path('login/', paginaLogin, name='login'),
    path('logout/', logout, name='logout'),
    path('cadastro/',paginaCadatro, name='cadastro'),
]
