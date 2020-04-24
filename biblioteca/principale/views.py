from django.shortcuts import render
from .models import Libro,LibriInDisuso,Collocazione,Sede,Stato,EDITORI,Autori,AutoreLibro,Utente,Prestito,Dewey,User
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'principale/index.html', {})

from django.views import generic
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

class FantasyList(generic.ListView):
    model = Libro
    paginate_by = 10 
    filtro=Libro.objects.filter(Genere='1')
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            filtro = self.model.objects.filter(Titolo=query,Genere='1')
        else:
            filtro = Libro.objects.filter(Genere='1')
        return filtro

class GialliList(generic.ListView):
    model = Libro
    paginate_by = 10 
    filtro=Libro.objects.filter(Genere='5')
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            filtro = self.model.objects.filter(Titolo=query,Genere='5')
        else:
            filtro = Libro.objects.filter(Genere='5')
        return filtro

class TuttiList(generic.ListView):
    model = Libro
    paginate_by = 10 
    filtro=Libro.objects.all()
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            filtro = self.model.objects.filter(Titolo=query)
        else:
            filtro = Libro.objects.all()
        return filtro



class RomanziList(generic.ListView):
    model = Libro
    paginate_by = 10 
    filtro=Libro.objects.filter(Genere='2')
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            filtro = self.model.objects.filter(Titolo=query,Genere='2')
        else:
            filtro = Libro.objects.filter(Genere='2')
        return filtro

def signin(request):
    numerolibri = Libro.objects.all().count()
    richiesta= Libro.objects.all().order_by('idLibro')
    librouno = richiesta[numerolibri - 1 ]
    librodue = richiesta[numerolibri - 2]
    librotre = richiesta[numerolibri - 3]
    libroquattro = richiesta[numerolibri - 4]
    utente= User.objects.first()
    context = {
        'librouno': librouno,
        'librodue': librodue,
        'librotre': librotre,
        'libroquattro': libroquattro,
        'utente': utente,
    }
    
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
                return render(request, 'principale/index.html', context=context)
    else:
        form = AuthenticationForm()
    return render(request, 'principale/login.html', {'form': form})
