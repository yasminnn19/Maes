from django.contrib import admin
from django.urls import path
from app.views import index, pagina_inicial  # Adicione a nova view

urlpatterns = [
    path('', index, name='index'),  # Página administrativa
    path('inicio/', pagina_inicial, name='pagina_inicial'),  # Página de usuários
    path('admin/', admin.site.urls),
]