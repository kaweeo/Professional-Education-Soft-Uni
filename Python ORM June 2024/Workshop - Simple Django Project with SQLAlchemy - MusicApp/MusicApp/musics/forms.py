from django import forms

from MusicApp.common.session_decorator import session_decorator
from MusicApp.musics.models import Album, Song
from MusicApp.settings import session


class AlbumBaseForm(forms.Form):
    album_name = forms.CharField(
        label='Album Name',
        max_length=30,
        required=True,
    )

    image_url = forms.URLField(
        label='Image URL:',
        max_length=30,
        required=True,
    )

    price = forms.DecimalField(
        label='Price',
        required=True,
        min_value=0.0,
    )


class AlbumCreateForm(AlbumBaseForm):

    @session_decorator(session)
    def save(self):
        new_album = Album(
            album_name=self.cleaned_data['album_name'],
            image_url=self.cleaned_data['image_url'],
            price=self.cleaned_data['price'],
        )

        session.add(new_album)

class SongBaseForm(forms.Form):
    song_name = forms.CharField(
        label='Song Name:',
        max_length=100,
        required=True,
    )

    album = forms.ChoiceField(
        label='Album:',
        choices=[],
    )

    # Over-riding the __init__ method so it can load the actual data from the DB
    # and store it like tuples in choices
    @session_decorator(session)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        albums = session.query(Album).all()
        self.fields['album'].choices = [(album.id, album.album_name) for album in albums]


class SongCreateForm(SongBaseForm):

    @session_decorator(session)
    def save(self):
        new_song = Song(
            song_name=self.cleaned_data['song_name'],
            album_id=self.cleaned_data['album'],
        )

        session.add(new_song)

class AlbumEditForm(AlbumBaseForm):
    def save(self, album):
        album.album_name = self.cleaned_data['album_name']
        album.image_url = self.cleaned_data['image_url']
        album.price = self.cleaned_data['price']

class AlbumDeleteForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['disabled'] = True


