# config/urls.py

from django.contrib import admin
from django.urls import path
from app.views import index, pagina_inicial, lista_dicas_nutricionais, detalhe_dica_nutricional, lista_postagens_forum, lista_receitas, detalhe_receita

urlpatterns = [
    path('', index, name='index'),
    path('inicio/', pagina_inicial, name='pagina_inicial'),
    path('admin/', admin.site.urls),
    path('dicas/', lista_dicas_nutricionais, name='lista_dicas'),
    path('dicas/<int:pk>/', detalhe_dica_nutricional, name='detalhe_dica'),
    path('forum/', lista_postagens_forum, name='lista_postagens'), 
    path('receitas/', lista_receitas, name='lista_receitas'),
    path('receitas/<int:pk>/', detalhe_receita, name='detalhe_receita'),
]