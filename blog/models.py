from django.db import models
# from django.db.models import Model
from django.urls import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import truncatechars

# Create your models here.


class postagem(models.Model):
    data_postagem = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    autor = models.ForeignKey('autor', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-data_postagem']

    def get_absolute_url(self):
        return reverse('postagem-detail', args=[str(self.id)])

    def __str__(self):
        return self.titulo


class autor(models.Model):
    nome = models.CharField(max_length=100)
    bio = models.TextField()
    data_registro = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('autor-detail', args=[str(self.id)])

    def __str__(self):
        return self.nome


class comentario(models.Model):
    conteudo = models.TextField()

    @property
    def conteudo_preview(self):
        return truncatechars(self.conteudo, 75)

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_comentario = models.DateTimeField(auto_now_add=True)
    postagem = models.ForeignKey(postagem, on_delete=models.CASCADE)

    class Meta:
        ordering = ['data_comentario']
