from django.contrib import admin

from .models import Avaliacao, Curso

# Register your models here.


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'url', 'cricao', 'atualizacao', 'ativo')

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('curso', 'nome','email','avaliacao', 'cricao', 'atualizacao', 'ativo')