from django.contrib import admin

# Register your models here.

from .models import autor, postagem, comentario


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('data_comentario', 'postagem', 'conteudo_preview')


class ComentarioInLine(admin.TabularInline):
    model = comentario


class PostagemAdmin(admin.ModelAdmin):
    list_display = ('data_postagem', 'titulo', 'autor')
    inlines = [ComentarioInLine]


class PostagemInline(admin.TabularInline):
    model = postagem
    fields = ('data_postagem', 'titulo')


class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_registro')
    inlines = [PostagemInline]


admin.site.register(postagem, PostagemAdmin)
admin.site.register(comentario, ComentarioAdmin)
admin.site.register(autor, AutorAdmin)
