from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    data_nascimento = models.DateField(null=True, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='usuarios_groups',
        related_query_name='usuario',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='usuarios_permissions',
        related_query_name='usuario',
    )

    def __str__(self):
        return self.username

# Modelo Alergia deve vir ANTES de Receita
class Alergia(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    
    def __str__(self):
        return self.nome

class Receita(models.Model):
    DIFICULDADE_CHOICES = [
        ('FACIL', 'Fácil'),
        ('MEDIO', 'Médio'),
        ('DIFICIL', 'Difícil'),
    ]
    
    titulo = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.PositiveIntegerField(help_text="Tempo em minutos")
    dificuldade = models.CharField(max_length=7, choices=DIFICULDADE_CHOICES)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    alergias_evitadas = models.ManyToManyField(Alergia, blank=True)  # Agora Alergia está definida
    imagem = models.ImageField(upload_to='receitas/', blank=True, null=True)
    
    def __str__(self):
        return self.titulo

# Restante dos modelos...
class TopicoForum(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    topico = models.ForeignKey(TopicoForum, on_delete=models.CASCADE)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comentário de {self.autor} em {self.topico.titulo}"