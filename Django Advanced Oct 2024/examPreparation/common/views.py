from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import BaseFormView
from albums.models import Album
from examPreparation.utils import get_user_obj
from profiles.forms import CreateProfileForm


class HomePage(ListView, BaseFormView):
    model = Album
    form_class = CreateProfileForm
    success_url = reverse_lazy('home')

    # Implemented via template tag
    # def get_context_data(self, *, object_list=None, **kwargs):  # EXTRA ADDED TO CHECK IF
    #     context = super().get_context_data()  # PROFILE, THEN ADD TO CONTEXT
    #     context['profile'] = get_user_obj()  # AND USE 'profile' in the template
    #     return context

    def get_template_names(self):
        profile = get_user_obj()  # Returns None or QuerySet

        if profile:
            return ['profiles/home-with-profile.html']

        return ['profiles/home-no-profile.html']

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
