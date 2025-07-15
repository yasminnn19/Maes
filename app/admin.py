from django.contrib import admin
from .models import Usuario, Alergia, Receita, TopicoForum, Comentario

admin.site.register(Usuario)
admin.site.register(Alergia)
admin.site.register(Receita)
admin.site.register(TopicoForum)
admin.site.register(Comentario)