
from django.urls import path
from .views import FilmeAno, FilmeCategoria, FilmeLingua, FilmeLista,FilmeDetalhe, FilmePesquisa


app_name ='filmes'
urlpatterns = [
    path('', FilmeLista.as_view(), name='filme_lista'),
    path('categoria/<str:categoria>', FilmeCategoria.as_view(), name='filme_categoria'), 
    path('pesquisa/', FilmePesquisa.as_view(), name='filme_pesquisa'), 
    path('lingua/<str:lingua>', FilmeLingua.as_view(), name='filme_lingua'),
    path('<slug:slug>', FilmeDetalhe.as_view(), name='filme_detalhe'),
    path('ano/<int:year>', FilmeAno.as_view(), name='filme_ano'),
] 
