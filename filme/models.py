from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.

LISTA_CATEGORIAS = (
    ("ANALISES", "Análises"),
    ("PROGRAMACAO", "Programação"),
    ("APRESENTACAO", "Apresentação"),
    ("OUTROS", "Outros"),
)

# criar o filme
class Filme(models.Model):
    objects = None
    thumb = models.ImageField(upload_to='thumb_filmes')
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo

# criar os espisodios
class Episodio(models.Model):
    filme = models.ForeignKey("Filme", related_name="episodios", on_delete=models.CASCADE)  # sempre deixar o campo com a chave estrangeira sendo o primeiro, esse campo cria um item de "Filme" com vários "Episódios" atrelados a ele.
    titulo = models.CharField(max_length=100)
    video = models.URLField()

    def __str__(self):
        return self.filme.titulo + " - " + self.titulo

class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField("Filme")