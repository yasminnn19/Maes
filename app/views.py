from django.shortcuts import render
from .models import Usuario, Receita, Ingrediente

def index(request):
    context = {
        'total_usuarios': Usuario.objects.count(),
        'total_receitas': Receita.objects.count(),
        'total_ingredientes': Ingrediente.objects.count()
    }
    return render(request, 'index.html', context)

def pagina_inicial(request):
    receitas_destaque = Receita.objects.all()[:3]  # 3 receitas mais recentes
    return render(request, 'inicio.html', {'receitas': receitas_destaque})