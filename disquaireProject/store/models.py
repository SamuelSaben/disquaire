from django.db import models


class Artist(models.Model):
    name = models.CharField('Nom', max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Artiste"


class Contact(models.Model):
    email = models.EmailField(max_length=100)
    name = models.CharField('Nom', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Client"

class Album(models.Model):
    reference = models.IntegerField(null=True)
    created_at = models.DateTimeField('Date de Creation', auto_now_add=True)
    available = models.BooleanField('Disponibilite', default=True)
    title = models.CharField('Titre', max_length=200)
    picture = models.URLField('URL image')
    artists = models.ManyToManyField(Artist, related_name='albums', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Album"

class Booking(models.Model):
    created_at = models.DateTimeField('Date Creation' , auto_now_add=True)
    contacted = models.BooleanField('Client Contacte', default=False)
    album = models.OneToOneField(Album, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return self.contact.name

    class Meta:
        verbose_name = "Reservation"