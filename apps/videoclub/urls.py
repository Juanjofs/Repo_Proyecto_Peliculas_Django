
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.auth.decorators import login_required

from apps.videoclub.views import *

urlpatterns = [
    path(
        '',
        login_required(VideoclubIndex.as_view()),
        name='index'
    ),
    path(
        'pelicula/<int:pk>/',
        login_required(PeliculaDetailView.as_view()),
        name='pelicula'
    ),
    path(
        'director/<int:pk>/',
        login_required(DirectorDetailView.as_view()),
        name='director'
    ),
    path(
        'actor/<int:pk>/',
        login_required(ActorDetailView.as_view()),
        name='actor'
    ),
    path(
        'peliculas/',
        login_required(PeliculasList.as_view()),
        name='peliculas'
    ),
    path(
        'directores/',
        login_required(DirectoresList.as_view()),
        name='directores'
    ),
    path(
        'actores/',
        login_required(ActoresList.as_view()),
        name='actores'
    ),
    path(
        'forbidden/',
        login_required(Forbidden.as_view()),
        name='forbidden'
    ),
    path(
        'peliculas/manage/',
        PeliculasManage.as_view(),
        name='peliculas_manage'
    ),
    path(
        'peliculas/manage/edit/<int:pk>/',
        PeliculasEdit.as_view(),
        name='peliculas_edit'
    ),
    path(
        'peliculas/manage/delete/<int:pk>/',
        PeliculasDelete.as_view(),
        name='peliculas_delete'
    ),
    path(
        'peliculas/manage/create',
        PeliculasCreate.as_view(),
        name='peliculas_create'
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
