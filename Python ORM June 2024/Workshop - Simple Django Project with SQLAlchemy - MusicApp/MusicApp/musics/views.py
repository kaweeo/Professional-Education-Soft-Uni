from django.http import HttpResponse
from django.shortcuts import render, redirect

from MusicApp.common.session_decorator import session_decorator
from MusicApp.musics.forms import SongCreateForm, AlbumCreateForm, AlbumEditForm, AlbumDeleteForm
from MusicApp.musics.models import Album, Song

from MusicApp.settings import session


# Create your views here.
@session_decorator(session)
def index(request):
    albums = session.query(Album).all()

    context = {
        'albums': albums,
    }

    return render(request, 'common/index.html', context)


def create_album(request):
    if request.method == 'GET':
        form = AlbumCreateForm()
    else:
        form = AlbumCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'albums/create-album.html', context)


@session_decorator(session)
def edit_album(request, pk: int):
    album = session.query(Album).get(pk)  # CARE

    if request.method == 'GET':
        form = AlbumEditForm(initial={
            'album_name': album.album_name,
            'image_url': album.image_url,
            'price': album.price,
        })
    else:
        form = AlbumEditForm(request.POST)

        if form.is_valid():
            form.save(album)
            return redirect('index')

    context = {
        'album': album,
        'form': form,
    }

    return render(request, 'albums/edit-album.html', context)


def delete_album(request, pk: int):
    album = session.query(Album).get(pk)  # CARE

    if request.method == 'GET':
        form = AlbumDeleteForm(initial={
            'album_name': album.album_name,
            'image_url': album.image_url,
            'price': album.price,
        })
    else:
        form = AlbumDeleteForm(request.POST)

        if form.is_valid():
            session.delete(album)
            return redirect('index')

    context = {
        'album': album,
        'form': form,
    }

    return render(request, 'albums/delete-album.html', context)


@session_decorator(session)
def album_details(request, pk: int):
    album = session.query(Album).filter_by(id=pk).first()
    context = {
        'album': album,
    }
    return render(request, 'albums/album-details.html', context)


def create_song(request):
    if request.method == 'GET':
        form = SongCreateForm()
    else:
        form = SongCreateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save(request)
            return redirect('index')
    context = {
        'form': form,
    }

    return render(request, 'songs/create-song.html', context)

@session_decorator(session)
def play_song(request, pk: int):
    song = session.query(Song).filter_by(id=pk).first()
    context = {
        'song': song,
    }

    return render(request, 'songs/music-player.html', context)

@session_decorator(session)
def server_song(request, pk: int):
    song = session.query(Song).filter_by(id=pk).first()
    if song:
        response = HttpResponse(song.music_file_data, content_type='audio/mpeg')
        response['Content-Disposition'] = f'inline; filename="{song.name}"'
        return response
    else:
        return HttpResponse('Song not found', status=404)

