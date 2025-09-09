from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, CategoriaReceita, Receita, Ingrediente, Favorito, Postagem, DicaNutricional

# INLINES
class ReceitaInline(admin.TabularInline):
    model = Receita
    extra = 0
    fields = ['nome', 'tempo_preparo', 'porcoes', 'categoria', 'data_criacao']
    readonly_fields = ['data_criacao']
    can_delete = False
    show_change_link = True

class FavoritoInline(admin.TabularInline):
    model = Favorito
    extra = 0
    fields = ['receita', 'data_adicao']
    readonly_fields = ['data_adicao']
    can_delete = False
    show_change_link = True

class PostagemInline(admin.TabularInline):
    model = Postagem
    extra = 0
    fields = ['resumo_texto', 'data_publicacao']
    readonly_fields = ['resumo_texto', 'data_publicacao']
    
    def resumo_texto(self, obj):
        return obj.texto[:50] + '...' if len(obj.texto) > 50 else obj.texto
    resumo_texto.short_description = 'Resumo'

class ReceitaCategoriaInline(admin.TabularInline):
    model = Receita
    extra = 0
    fields = ['nome', 'autor', 'tempo_preparo', 'data_criacao']
    readonly_fields = ['data_criacao']
    can_delete = False
    show_change_link = True

# ADMIN CLASSES
class UsuarioAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        ('Preferências', {'fields': ('preferencias_alimentares',)}),
    )
    inlines = [ReceitaInline, FavoritoInline, PostagemInline]
    filter_horizontal = ()

class CategoriaReceitaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'contar_receitas')
    search_fields = ('nome',)
    ordering = ('nome',)
    inlines = [ReceitaCategoriaInline]
    
    def contar_receitas(self, obj):
        return obj.receitas.count()
    contar_receitas.short_description = 'Nº de Receitas'

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

# admin.py - adicione estas linhas

from .models import DicaNutricional

class DicaNutricionalAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'data_criacao']
    list_filter = ['data_criacao']
    search_fields = ['titulo', 'texto']





# REGISTROS
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(CategoriaReceita, CategoriaReceitaAdmin)
admin.site.register(Ingrediente, IngredienteAdmin)
admin.site.register(Receita, ReceitaAdmin)
admin.site.register(Favorito, FavoritoAdmin)
admin.site.register(Postagem, PostagemAdmin)
admin.site.register(DicaNutricional)
