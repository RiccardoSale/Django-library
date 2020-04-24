from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
class Libro(models.Model):
    idLibro= models.AutoField(primary_key= True)
    Dewey= models.ForeignKey('Dewey',on_delete=models.CASCADE)
    Titolo = models.CharField(max_length=200)
    Isbn= models.IntegerField()
    Editore= models.ForeignKey('EDITORI', on_delete=models.CASCADE)
    Autore=models.ForeignKey('Autori',on_delete=models.CASCADE)
    Nedizione= models.IntegerField()
    AnnoPubblicazione= models.IntegerField()
    Luogopubblicazione=models.CharField(max_length=30)
    Prezzo=models.IntegerField()
    DataAcquisto=models.DateTimeField(auto_now=True)
    Descrizione=models.CharField(max_length=2000)
    Pagine=models.IntegerField()
    idCollocazione=models.ForeignKey('Collocazione',on_delete=models.CASCADE)
    IdSede=models.ForeignKey('Sede',on_delete=models.CASCADE)
    BOOL_CHOICES = ((True, 'si'), (False, 'no'))
    InPrestito= models.BooleanField(choices=BOOL_CHOICES)
    idStato=models.ForeignKey('Stato',on_delete=models.CASCADE)
    image=models.ImageField(blank=True,null=True)
    Genere= models.ForeignKey('Generi',on_delete=models.CASCADE)
    def __str__(self):
        return self.Titolo
    def get_absolute_url(self):
        return reverse('Libri-dettagli', args=[str(self.idLibro)])
    class Meta:
        verbose_name_plural = "LIBRI"

class EDITORI(models.Model):
    IdEditore = models.AutoField(primary_key= True )
    editore = models.CharField(max_length=50)

    def __str__(self):
        return self.editore
    class Meta:
        verbose_name_plural= "EDITORI"

class Generi(models.Model):
    IdGenere = models.AutoField(primary_key= True )
    genere = models.CharField(max_length=50)

    def __str__(self):
        return self.genere
    class Meta:
        verbose_name_plural= "Generi"

class Sede(models.Model):
    IdSede= models.AutoField(primary_key= True)
    Sede=models.CharField(max_length=20)

    def __str__(self):
        return self.Sede
    class Meta:
        verbose_name_plural= "SEDI"

class Stato(models.Model):
    idStato= models.AutoField(primary_key= True)
    Stato=models.CharField(max_length=20)

    def __str__(self):
        return self.Stato
    class Meta:
        verbose_name_plural= "STATI"

class Collocazione(models.Model):
    idCollocazione=models.AutoField(primary_key= True)
    Collocazione=models.CharField(max_length=20)
    def __str__(self):
        return self.Collocazione
    class Meta:
        verbose_name_plural= "COLLOCAZIONI"

class LibriInDisuso(models.Model):
    idLibro=models.ForeignKey('Libro',on_delete= True)
    Data=models.DateTimeField(auto_now=False)
    Motivo=models.CharField(max_length=1000)

    def __str__(self):
        return str(self.idLibro)
    class Meta:
        verbose_name_plural="LIBRI In DISUSO"

class Autori(models.Model):
    idAutore= models.AutoField(primary_key=True)
    CognomeNome= models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('Autori-dettagli', args=[str(self.idAutore)])

    def __str__(self):
        return self.CognomeNome
    class Meta:
        verbose_name_plural='AUTORI'
        
class Utente(models.Model):
    idUtente= models.AutoField(primary_key=True)
    CognomeNome=models.CharField(max_length=255)
    Classe=models.CharField(max_length=80)
    
    def __str__(self):
        return self.CognomeNome
    class Meta:
        verbose_name_plural='UTENTI'

class AutoreLibro(models.Model):
    Idlibro=models.ForeignKey('Libro',on_delete=models.CASCADE)
    idAutore=models.ForeignKey('Autori',on_delete=models.CASCADE)

    def __str__(self):
        return  str(self.Idlibro) + "-" + str(self.idAutore)

    class Meta:
        verbose_name_plural="AUTORI-LIBRI"


class Prestito(models.Model):
    idPrestito=models.AutoField(primary_key=True)
    idlibro=models.ForeignKey('Libro',on_delete=models.CASCADE)
    idutente=models.ForeignKey('Utente',on_delete=models.CASCADE)
    dataPrelievo=models.DateTimeField(null=True)
    dataRestituzione=models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return str(self.idutente)+"_"+ str(self.dataPrelievo)

    class Meta:
    	verbose_name_plural="PRESTITI"


class Dewey(models.Model):
    codiceDewey=models.CharField(primary_key=True,max_length=3)
    Dewey=models.CharField(max_length=20)

    def __str__(self):
         return self.Dewey
    
    class Meta:
        verbose_name_plural="CodiciDewey"

