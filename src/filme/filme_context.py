from . models import Filme


def slider_filme(request):
    filme = Filme.objects.all().order_by('created')[0:5]
    return{'slider_filme': filme}