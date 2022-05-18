from django.utils.text import slugify
from django.db import models
from django.utils import timezone

STATUS_CHOICES=(
    ('RA','Recem Adicionado'),
    ('MA','Mais Assistidos'),
    ('TR','Top Rated')
)


CATEGORIA_CHOICES=(
    ('ação','Ação'),
    ('romance','Romance'),
    ('ficção','Ficção'),
    ('terror','Terror'),
    ('aventura','Aventura'),
    ('suspense','Suspense'),
    ('anime','Anime'),
)

LINGUA_CHOICES = (
    ('Português','PT-BR'),
    ('Inglês','EN'),
    ('Espanhol','ESP'),
    ('Japônes','JP'),
)

#Tabela Filmes
class Filme(models.Model):
    titulo= models.CharField(max_length=100)
    descricao=models.TextField(max_length=1000)
    views_count= models.IntegerField(default=0)
    imagem= models.ImageField(upload_to='filmes')
    banner= models.ImageField(upload_to='filmes_banner')
    categoria=models.CharField(choices=CATEGORIA_CHOICES, max_length=9)
    lingua=models.CharField(choices=LINGUA_CHOICES,max_length=10)
    ano_de_producao= models.DateField()
    status=models.CharField(choices=STATUS_CHOICES,max_length=9)
    atores= models.CharField(max_length=100)
    slug =models.SlugField(blank=True, null=True)
    filme_trailer = models.URLField()
    #tags=
    created=models.DateTimeField(default=timezone.now)


    def save(self, *args , **kawrgs):
        if not self.slug :
            self.slug = slugify(self.titulo)
        super(Filme,self).save(*args , **kawrgs)



    def __str__(self) -> str:
        return self.titulo

LINK_CHOICES = (
     ('D','DOWNLOAD'),
     ('A','ASSISTIR')
)
#Dowloand e Assitir Filmes 
class FilmeLinks(models.Model):
    filme = models.ForeignKey(Filme,related_name='filme_assista_link',on_delete=models.CASCADE)
    type = models.CharField(choices=LINK_CHOICES, max_length=1)
    link = models.URLField()

    def __str__(self):
        return str(self.filme)
