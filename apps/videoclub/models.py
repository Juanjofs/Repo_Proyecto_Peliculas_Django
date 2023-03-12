from django.db import models
from django.utils.safestring import mark_safe
from django.conf import settings
from datetime import date
import re


class Actor(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(
        'Fecha de nacimiento'
    )
    fecha_defuncion = models.DateField(
        'Fallecido',
        null=True,
        blank=True,
    )
    foto = models.ImageField(
        upload_to='images/actores/',
        default='images/actores/sin_foto.jpg'
    )

    def image_admin(self):
        return mark_safe("<img style='max-width:220px; max-height:300px' src=\"{}\" />".format(settings.MEDIA_URL+str(self.foto)))

    image_admin.short_description = 'Foto actual'

    def url_foto(self):
        return settings.MEDIA_URL+str(self.foto)

    def get_edad(self):
        today = date.today()
        return today.year - self.fecha_nacimiento.year - ((today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))

    def get_num_peliculas(self):
        n_peliculas = self.pelicula_set.count()
        return n_peliculas

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Actores"

class Director(models.Model):
    nombre = models.CharField(
        max_length=100
    )
    fecha_nacimiento = models.DateField()
    fecha_defuncion = models.DateField(
        'Fallecido',
        null=True,
        blank=True,
    )
    foto = models.ImageField(
        upload_to='images/directores/',
        default='images/directores/sin_foto.jpg'
    )

    def image_admin(self):
        return mark_safe("<img style='max-width:220px; max-height:300px' src=\"{}\" />".format(settings.MEDIA_URL+str(self.foto)))

    image_admin.short_description = 'Foto actual'

    def get_edad(self):
        today = date.today()
        return today.year - self.fecha_nacimiento.year - ((today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))

    def url_foto(self):
        return settings.MEDIA_URL+str(self.foto)

    def get_num_peliculas(self):
        n_peliculas = self.pelicula_set.count()
        return n_peliculas

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Directores"

class Genero(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Géneros"

class Pelicula(models.Model):
    titulo = models.CharField(
        max_length=100
    )
    url_trailer = models.CharField(
        max_length=100
    )
    fecha = models.DateField()
    notas_posibles = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )
    nota = models.IntegerField(
        default=3,
        choices=notas_posibles
    )
    sinopsis = models.TextField(
        max_length=400,
        default="Sin sinopsis"
    )
    caratula = models.ImageField(
        upload_to='images/peliculas/caratulas',
        default='images/peliculas/caratulas/sin_caratula.jpg'
    )
    imagen_promocional = models.ImageField(
        upload_to='images/peliculas/imagenes_promocionales',
        default='images/peliculas/imagenes_promocionales/sin_imagen.jpg'
    )
    genero = models.ManyToManyField(
        Genero,
        blank=True,
        related_name='genero'
    )
    director = models.ForeignKey(
        Director,
        on_delete=models.SET('Sin Director')
    )
    actores = models.ManyToManyField(
        Actor,
        blank=True
    )
    

    def caratula_admin(self):
        return mark_safe("<img style='max-width:220px; max-height:300px' src=\"{}\" />".format(settings.MEDIA_URL+str(self.caratula)))

    caratula_admin.short_description = 'Carátula actual'

    def imagen_promocional_admin(self):
        return mark_safe("<img style='max-width:220px; max-height:300px' src=\"{}\" />".format(settings.MEDIA_URL+str(self.imagen_promocional)))

    imagen_promocional_admin.short_description = 'Imágen promocional actual'

    def url_imagen_promocional(self):
        return settings.MEDIA_URL+str(self.imagen_promocional)

    def url_caratula(self):
        return settings.MEDIA_URL+str(self.caratula)
  
    def nota_html(self):
        html = ""
        nota = int(self.nota)
        if nota == 1:
                html += "<i title='item' class='fas fa-star text-warning'></i>"
        else:
            for item in range(nota):
                html += "<i title='probando' class='fas fa-star text-warning'></i>"

        return mark_safe(html)
    
    def video_id(self, url_trailer):

        regex = re.compile(r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)?(?P<id>[A-Za-z0-9\-=_]{11})')

        match = regex.match(url_trailer)

        if not match:
            return False

        return mark_safe(match.group('id'))

    def trailer_embed(self):
        id_video = self.video_id(self.url_trailer)
        code = "<iframe width=\"560\" height=\"315\" src=\"https://www.youtube.com/embed/"+id_video+"\" frameborder=\"0\" allow=\"accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe>"
        return mark_safe(code)

    def __str__(self):
        return self.titulo

    class Meta():
        verbose_name_plural = "Películas"

class Copia(models.Model):
    fecha_llegada = models.DateField()
    pelicula = models.ForeignKey(
        Pelicula,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "(id: {}) {}".format(self.id, self.pelicula.titulo)

    class Meta:
        verbose_name_plural = "Copias"
