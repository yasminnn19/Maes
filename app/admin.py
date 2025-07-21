from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, CategoriaReceita, Receita, Ingrediente, Favorito, Postagem

class UsuarioAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        ('Preferências', {'fields': ('preferencias_alimentares',)}),
    )
    filter_horizontal = ()

class CategoriaReceitaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    ordering = ('nome',)

class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome', 'substituicoes_sugeridas')
    ordering = ('nome',)

class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'autor', 'tempo_preparo', 'porcoes', 'data_criacao')
    list_filter = ('categoria', 'data_criacao')
    search_fields = ('nome', 'ingredientes', 'modo_preparo')
    raw_id_fields = ('autor',)
    date_hierarchy = 'data_criacao'
    filter_horizontal = ()

class FavoritoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'receita', 'data_adicao')
    list_filter = ('data_adicao',)
    raw_id_fields = ('usuario', 'receita')
    date_hierarchy = 'data_adicao'

class PostagemAdmin(admin.ModelAdmin):
    list_display = ('autor', 'resumo_texto', 'data_publicacao')
    list_filter = ('data_publicacao',)
    search_fields = ('texto',)
    raw_id_fields = ('autor',)
    date_hierarchy = 'data_publicacao'
    
    def resumo_texto(self, obj):
        return obj.texto[:50] + '...' if len(obj.texto) > 50 else obj.texto
    resumo_texto.short_description = 'Resumo'

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(CategoriaReceita, CategoriaReceitaAdmin)
admin.site.register(Ingrediente, IngredienteAdmin)
admin.site.register(Receita, ReceitaAdmin)
admin.site.register(Favorito, FavoritoAdmin)
admin.site.register(Postagem, PostagemAdmin)