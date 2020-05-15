from django.views import generic
from django.shortcuts import render
from .models import Libro, LibriInDisuso, Collocazione, Sede, Stato, EDITORI, Autori, AutoreLibro, Utente, Prestito, Dewey, User
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import JsonResponse


class BookList(generic.ListView):
    model = Libro
    model = Autori
    paginate_by = 20

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            filtro = (Libro.objects.filter(Autore__CognomeNome__contains=query)
                      | Libro.objects.filter(Titolo__contains=query))
        else:
            filtro = Libro.objects.all()
        return filtro


class FantasyList(generic.ListView):
    model = Libro
    paginate_by = 10
    filtro = Libro.objects.filter(Genere='1')

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            filtro = (self.model.objects.filter(Titolo__contains=query, Genere='1')
                      | Libro.objects.filter(Autore__CognomeNome__contains=query, Genere='1'))
        else:
            filtro = Libro.objects.filter(Genere='1')
        return filtro


class GialliList(generic.ListView):
    model = Libro
    paginate_by = 10
    filtro = Libro.objects.filter(Genere='5')

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            filtro = (self.model.objects.filter(Titolo__contains=query, Genere='5')
                      | Libro.objects.filter(Autore__CognomeNome__contains=query, Genere='5'))
        else:
            filtro = Libro.objects.filter(Genere='5')
        return filtro


class TuttiList(generic.ListView):
    model = Libro
    model = Autori
    paginate_by = 20

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            filtro = (Libro.objects.filter(Autore__CognomeNome__contains=query)
                      | Libro.objects.filter(Titolo__contains=query))
        else:
            filtro = Libro.objects.all()
        return filtro


class RomanziList(generic.ListView):
    model = Libro
    paginate_by = 10
    filtro = Libro.objects.filter(Genere='2')

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            filtro = (self.model.objects.filter(Titolo__contains=query, Genere='2')
                      | Libro.objects.filter(Autore__CognomeNome__contains=query, Genere='2'))
        else:
            filtro = Libro.objects.filter(Genere='2')
        return filtro


def signin(request):
    numerolibri = Libro.objects.all().count()
    richiesta = Libro.objects.all().order_by('idLibro')
    librouno = richiesta[numerolibri - 1]
    librodue = richiesta[numerolibri - 2]
    librotre = richiesta[numerolibri - 3]
    libroquattro = richiesta[numerolibri - 4]
    context = {
        'librouno': librouno,
        'librodue': librodue,
        'librotre': librotre,
        'libroquattro': libroquattro,
    }

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user.is_active:
            login(request, user)
            return render(request, 'principale/index.html', context)
    else:
        return render(request, 'principale/login.html',)
