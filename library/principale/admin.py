
from django.contrib import admin

from .models import Libro,LibriInDisuso,Collocazione,Sede,Stato,EDITORI,Autori,AutoreLibro,Utente,Prestito,Dewey,Generi

admin.site.register(Collocazione)

admin.site.register(Sede)

admin.site.register(Stato)

admin.site.register(EDITORI)

admin.site.register(Autori)

admin.site.register(Generi)

class AdminLibro(admin.ModelAdmin):
    list_display=['Isbn','Titolo','Autore','Editore','AnnoPubblicazione']

admin.site.register(Libro,AdminLibro)

class AdminUtenti(admin.ModelAdmin):
    list_display=['idUtente','CognomeNome','Classe']


admin.site.register(Utente,AdminUtenti)


class AdminDisuso(admin.ModelAdmin):
    list_display=['idLibro','Data','Motivo']


admin.site.register(LibriInDisuso,AdminDisuso)

class AdminPrestito(admin.ModelAdmin):
     list_display=['idlibro','idutente','dataPrelievo','dataRestituzione']


admin.site.register(Prestito,AdminPrestito)


class AdminDewey(admin.ModelAdmin):
     list_display=['codiceDewey','Dewey']

admin.site.register(Dewey,AdminDewey)