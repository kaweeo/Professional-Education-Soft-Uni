from django import forms

from MusicApp.common.session_decorator import session_decorator
from MusicApp.musics.models import Album
from MusicApp.settings import session


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

    @session_decorator(session)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        albums = session.query(Album).all()
        self.fields['album'].choices = [(album.id, album.album_name) for album in albums]


class SongCreateForm(SongBaseForm):
    pass
