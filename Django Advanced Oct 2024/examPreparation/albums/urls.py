from django.urls import path, include

from albums.forms import EditAlbumForm
from albums.views import AlbumCreateView, AlbumDetailsView, AlbumEditView, AlbumDeleteView

urlpatterns = [
    path('add/', AlbumCreateView.as_view(), name='add-album'),
    path('<int:id>/', include([
        path('edit/', AlbumEditView.as_view(), name='album-edit'),
        path('details/', AlbumDetailsView.as_view(), name='album-details'),
        path('delete/', AlbumDeleteView.as_view(), name='album-delete'),
    ]))
]
