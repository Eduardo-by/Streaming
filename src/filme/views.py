from urllib.request import Request
from django.views.generic import ListView, DetailView
from django.views.generic.dates import YearArchiveView
from django.core.paginator import Paginator

from .models import  Filme ,FilmeLinks

class HomeView(ListView):
    model = Filme
    template_name = 'filme/home.html'

    def get_context_data(self,**kwargs):
       context = super(HomeView, self).get_context_data(**kwargs)
       context['mais_votados']=Filme.objects.filter(status = 'TR')
       context['mais_assistidos'] =Filme.objects.filter(status = 'MA')
       context['recem_adicionados'] =Filme.objects.filter(status = 'RA')
        
       return context


class FilmeLista(ListView):
    model = Filme
    paginate_by = 15


class FilmeDetalhe(DetailView):
    model =Filme

    
    def get_object(self):
        object = super(FilmeDetalhe, self).get_object()
        object.views_count +=1
        object.save()
        return object
    
    def get_context_data(self,**kwargs):
        context=super(FilmeDetalhe, self).get_context_data(**kwargs)
        context['links'] = FilmeLinks.objects.filter(filme=self.get_object())
        context ['filmes_relacionados'] = Filme.objects.filter(categoria = self.get_object().categoria)#.order_by['created'][0:6]
        
        return context

class FilmeCategoria(ListView):

    model = Filme
    paginate_by = 15

    def get_queryset(self):
        self.categoria = self.kwargs['categoria']
        filmes = Filme.objects.filter(categoria=self.categoria)
        return filmes

    def get_context_data(self,**kwargs):
       context = super(FilmeCategoria, self).get_context_data(**kwargs)
       context['filme_categoria'] = self.categoria
       return context

class FilmeLingua(ListView):

    model = Filme
    paginate_by = 15

    def get_queryset(self):
        self.lingua = self.kwargs['lingua']
        filmes = Filme.objects.filter(lingua=self.lingua)
        return filmes

    def get_context_data(self,**kwargs):
       context = super(FilmeLingua, self).get_context_data(**kwargs)
       context['filme_lingua'] = self.lingua
       return context

class FilmePesquisa(ListView):

    model = Filme
    paginate_by = 15

    def get_queryset(self):
        query =self.request.GET.get('q')
        if query:
            object_list = Filme.objects.filter(titulo__icontains=query)
        else:
            object_list= self.model.objects.none()
        return object_list

class FilmeAno(YearArchiveView):
    paginate_by = 15
    queryset = Filme.objects.all()
    date_field = 'ano_de_producao'
    make_object_list =True
    allow_future=True