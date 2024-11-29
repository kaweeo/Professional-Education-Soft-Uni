from django.contrib.auth import get_user
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView
from examPreparation.utils import get_user_obj
from profiles.models import Profile


class ProfileDetailsView(DetailView):
    # model = Profile
    # template_name = 'profiles/profile-details.html'
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     return context

    template_name = 'profiles/profile-details.html'

    def get_object(self, queryset=None):  # We don't have pk or slug for DetailView requirements
        return get_user_obj()  # We have only one profile in DB, our function is getting it


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'profiles/profile-delete.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return get_user_obj()


# class ProfileDeleteView(DeleteView):
#     model = Profile
#     template_name = 'profiles/profile-delete.html'
#     success_url = reverse_lazy('home')  # Redirect to the home page after deletion
#
#     def delete(self, request, *args, **kwargs):
#         """
#         Override the delete method to delete associated albums.
#         """
#         self.object = self.get_object()
#
#         # Delete all albums associated with the profile
#         Profile.objects.filter(profile=self.object).delete()
#
#         # Delete the profile itself
#         response = super().delete(request, *args, **kwargs)
#
#         return response