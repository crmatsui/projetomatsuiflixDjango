from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

LISTA_CATEGORIAS = (
    ("ANALISES", "Análises"), #"ANALISES" é como sera armazenado no banco de dados e "Análises" é como irá aparecer para o usuario
    ("PROGRAMACAO", "Programação"),
    ("APRESENTACAO", "Apresentação"),
    ("OUTROS", "Outros"),
)
# SAO TUPLAS DENTRO DA LISTA_CATEGORIAS

# criar o filme
class Filme(models.Model):
    titulo = models.CharField(max_length=100) # titulo de um filme
    thumb = models.ImageField(upload_to='thumb_filmes')# envolve arquivos de imagem. ex: foto da capa do video do  youtube por ex. ou do filme/ serie . #thumb_filmes e a pasta onde sera armazenado essas imagens dos filmes/serie criadas    descricao = models.TextField(max_length=1000) # descricao de um filme ou serie, por isso mais caracteres
    descricao = models.TextField(max_length=1000,default=0)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS) #tamanho maximo de caracteres que sera armazenado no banco de dados. ex: "ANALISES""PROGRAMACAO" etc.
    visualizacoes = models.IntegerField(default=0) #quantidade de vizualizacoes
    data_criacao = models.DateTimeField(default=timezone.now) #melhor criar datatimefield do que so datefield, pois consigo saber data e horario que foi criado o filme. Se tiver sido criado dois filmes no mesmo dia, saberei qual foi criado primeiro que o outro pelo horario.
#default=timezonenow sem parenteses quer dizer que vc quer preencher data e horario da criação do filme de agora.


    def __str__(self):
        return self.titulo

   # essa funcao acima eu rodo para exibir o titulo do filme/apresentação/serie pois ao criar no admin do site, aparecera 'Filme object(1)'
# nao precisa rodar o migrate pois nao foi alterado nada no banco de dados.Porem se rodar nao tem problema pois nao ira dar erro

# criar os episodios

class Episodio(models.Model):
    filme = models.ForeignKey("Filme", related_name="episodios", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()

    def __str__(self):
        return self.filme.titulo + " - " + self.titulo

# criar o usuario
class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField("Filme")

