from django import forms

from examPreparation.mixins import PlaceholderMixin
from profiles.models import Profile


# class BaseProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['username', 'email', 'age']  # Same as fields = "__all__"
#         widgets = {
#             'username': forms.TextInput(attrs={'placeholder': 'Username'}),
#             'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
#             'age': forms.NumberInput(attrs={'placeholder': 'Age'}),
#         }


class BaseProfileForm(PlaceholderMixin, forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

class CreateProfileForm(BaseProfileForm):
    pass
