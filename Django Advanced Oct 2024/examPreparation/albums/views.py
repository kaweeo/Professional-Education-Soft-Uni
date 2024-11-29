from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from albums.forms import CreateAlbumForm, EditAlbumForm, DeleteAlbumForm
from albums.models import Album
from examPreparation.utils import get_user_obj


class AlbumCreateView(CreateView):
    model = Album
    form_class = CreateAlbumForm
    template_name = 'albums/album-add.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = get_user_obj()
        return super().form_valid(form)


class AlbumDetailsView(DetailView):
    model = Album
    pk_url_kwarg = 'id'
    template_name = 'albums/album-details.html'


class AlbumEditView(UpdateView):
    model = Album
    pk_url_kwarg = 'id'
    template_name = 'albums/album-edit.html'
    form_class = EditAlbumForm

    # success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')


class AlbumDeleteView(DeleteView):
    model = Album
    pk_url_kwarg = 'id'
    form_class = DeleteAlbumForm
    template_name = 'albums/album-delete.html'
    success_url = reverse_lazy('home')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):  # Returns an error while validating that instance with the same name already exists
        return self.form_valid(
            form)  # Returning always a valid form prevents validating errors while trying to delete the instance
