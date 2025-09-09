from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

class Usuario(AbstractUser):
    """Modelo de usuário personalizado com preferências alimentares"""
    preferencias_alimentares = models.TextField(
        'Preferências Alimentares', 
        blank=True, 
        null=True,
        help_text='Lista de preferências ou restrições alimentares'
    )
    
    def __str__(self):
        return self.username
    
class CategoriaReceita(models.Model):
    """Modelo para categorias de receitas (ex: sobremesas, vegetarianas, etc)"""
    nome = models.CharField(max_length=100, unique=True)
    
    class Meta:
        verbose_name = 'Categoria de Receita'
        verbose_name_plural = 'Categorias de Receitas'
        ordering = ['nome']
    
    def __str__(self):
        return self.nome
    
    # Adicione este método
    def contar_receitas(self):
        return self.receitas.count()
    
class Ingrediente(models.Model):
    """Modelo para ingredientes com sugestões de substituições"""
    nome = models.CharField(max_length=100, unique=True)
    substituicoes_sugeridas = models.TextField(
        'Substituições Sugeridas', 
        blank=True, 
        null=True,
        help_text='Lista de possíveis substituições para este ingrediente'
    )
    
    class Meta:
        ordering = ['nome']
    
    def __str__(self):
        return self.nome

class Receita(models.Model):
    """Modelo principal para receitas culinárias"""
    nome = models.CharField(max_length=200)
    ingredientes = models.TextField(help_text='Lista de ingredientes necessários')
    modo_preparo = models.TextField('Modo de Preparo')
    tempo_preparo = models.PositiveIntegerField(
        'Tempo de Preparo (minutos)',
        validators=[MinValueValidator(1)]
    )
    porcoes = models.PositiveIntegerField(
        'Porções',
        validators=[MinValueValidator(1)]
    )
    categoria = models.ForeignKey(
        CategoriaReceita, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='receitas'
    )
    autor = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='receitas_criadas'
    )
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-data_criacao']
        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'
    
    def __str__(self):
        return f"{self.nome} (por {self.autor.username})"

class Favorito(models.Model):
    """Modelo para relacionamento de usuários e receitas favoritas"""
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='receitas_favoritas'
    )
    receita = models.ForeignKey(
        Receita,
        on_delete=models.CASCADE,
        related_name='favoritada_por'
    )
    data_adicao = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('usuario', 'receita')
        verbose_name = 'Receita Favorita'
        verbose_name_plural = 'Receitas Favoritas'
        ordering = ['-data_adicao']
    
    def __str__(self):
        return f"{self.receita.nome} favorita por {self.usuario.username}"

class Postagem(models.Model):
    """Modelo para postagens de usuários no sistema"""
    texto = models.TextField()
    imagem = models.ImageField(
        upload_to='postagens/',
        blank=True,
        null=True
    )
    autor = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='postagens'
    )
    data_publicacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'
    
    def __str__(self):
        return f"Postagem de {self.autor.username} em {self.data_publicacao}"

# models.py - adicione este modelo junto com os existentes

class DicaNutricional(models.Model):
    """Modelo simples para dicas nutricionais como texto"""
    titulo = models.CharField(max_length=200)
    texto = models.TextField('Texto da Dica')
    autor = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='dicas_nutricionais'
    )
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-data_criacao']
        verbose_name = 'Dica Nutricional'
        verbose_name_plural = 'Dicas Nutricionais'
    
    def __str__(self):
        return self.titulo