from django.contrib import admin
from .models import Actor, Director, Genero, Pelicula, Copia

class ActorAdmin(admin.ModelAdmin):
    readonly_fields = ['image_admin']

admin.site.register(Actor, ActorAdmin)

class DirectorAdmin(admin.ModelAdmin):
    readonly_fields = ['image_admin']

admin.site.register(Director, DirectorAdmin)

class PeliculaAdmin(admin.ModelAdmin):
    readonly_fields = ['caratula_admin', 'imagen_promocional_admin']

admin.site.register(Pelicula, PeliculaAdmin)

admin.site.register(Genero)
admin.site.register(Copia)
