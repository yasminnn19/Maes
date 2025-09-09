from django.shortcuts import render
from django.shortcuts import render, get_object_or_404 
from .models import Usuario, Receita, Ingrediente, DicaNutricional, Postagem

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

# app/views.py

def lista_dicas_nutricionais(request):
    dicas = DicaNutricional.objects.all()
    return render(request, 'dicas/lista_dicas.html', {'dicas': dicas})
    # ↑ Mude de 'app/dicas/lista_dicas.html' para 'dicas/lista_dicas.html'

def detalhe_dica_nutricional(request, pk):
    dica = get_object_or_404(DicaNutricional, pk=pk)
    return render(request, 'dicas/detalhe_dica.html', {'dica': dica})
    # ↑ Mude de 'app/dicas/detalhe_dica.html' para 'dicas/detalhe_dica.html'

def lista_postagens_forum(request):
    postagens = Postagem.objects.all().order_by('-data_publicacao')
    return render(request, 'forum/lista_postagens.html', {'postagens': postagens})

# app/views.py

def lista_receitas(request):
    receitas = Receita.objects.all().order_by('-data_criacao')
    return render(request, 'receitas/lista_receitas.html', {'receitas': receitas})

def detalhe_receita(request, pk):
    receita = get_object_or_404(Receita, pk=pk)
    return render(request, 'receitas/detalhe_receita.html', {'receita': receita})