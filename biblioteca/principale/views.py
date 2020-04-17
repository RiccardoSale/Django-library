from django.shortcuts import render
from .models import Libro,LibriInDisuso,Collocazione,Sede,Stato,EDITORI,Autori,AutoreLibro,Utente,Prestito,Dewey
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext

def post_list(request):
    return render(request, 'principale/index.html', {}, RequestContext(request))

from django.views import generic
class BookListView(generic.ListView):
    model = Libro
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Libro
    def get_queryset(self):
        Libri = Libro.objects.all()
        query = self.request.GET.get('Titolo', None)
        if query:
           return Libri.filter(Titolo=query)
        return Libri

class BookList(generic.ListView):
    model = Libro
    paginate_by = 12
  

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(Titolo=query)
        else:
            object_list = self.model.objects.all()
        return object_list

class AuthorListView(generic.ListView):
    model = Autori
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    model = Autori
