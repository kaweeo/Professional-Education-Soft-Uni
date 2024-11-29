from django.forms import ModelForm

from albums.models import Album
from examPreparation.mixins import PlaceholderMixin, ReadOnlyMixin


class BaseAlbumForm(ModelForm):
    class Meta:
        model = Album
        exclude = ('owner', )
        widgets = {}


class CreateAlbumForm(BaseAlbumForm, PlaceholderMixin):
    pass


class DetailsAlbumForm(BaseAlbumForm):
    pass


class EditAlbumForm(BaseAlbumForm):
    pass


class DeleteAlbumForm(ReadOnlyMixin, BaseAlbumForm):
    read_only_fields = ['album_name', 'artist', 'genre', 'price', 'description']