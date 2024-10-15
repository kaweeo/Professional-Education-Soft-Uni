from django import forms

from forumApp.posts.mixins import DisableFieldsMixin
# from forumApp.posts.choices import LanguageChoice
from forumApp.posts.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

        error_messages = {
            'title': {
                'required': "Please enter the title of your post!",
                'max_length': f"Title too long! Please keep it under: {Post.TITLE_MAX_LENGTH}",
            },
            'author': {
                'required': "Please enter the author!",
            }
        }

class PostCreateForm(PostBaseForm):
    pass


class PostEditForm(PostBaseForm):
    pass


class PostDeleteForm(PostBaseForm, DisableFieldsMixin):
    # disabled_fields = ('title', 'author')
    disabled_fields = ('__all__', )


class SearchForm(forms.Form):
    query = forms.CharField(
        label="",
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Search for a post..."}),
    )

# # Example to see diff between ModelForm and Form
# class PostForm(forms.Form):
#     title = forms.CharField(
#         max_length=100,
#     )
#
#     content = forms.CharField(
#         widget=forms.Textarea,
#     )
#
#     author = forms.CharField(
#         max_length=30,
#     )
#
#     created_at = forms.DateTimeField()
#
#     languages = forms.CharField(
#         choices=LanguageChoice.choices,
#     )

# class PersonForm(forms.Form):
#     STATUS_CHOICES = (
#         (1, 'Draft'),
#         (2, 'Published'),
#         (3, 'Archived'),
#     )
#
#     person_name = forms.CharField(
#         # widget=forms.TextInput(
#         #     attrs={'class': 'form-control'}
#         # )
#         label='Person Name',
#         initial='<NAME>',
#     )
#
#     age = forms.IntegerField()
#
#     is_lecturer = forms.BooleanField()
#
#     # status = forms.IntegerField(
#     #     widget=forms.Select(choices=STATUS_CHOICES)
#     # )       # IntegerField + widget returns ints, ChoiceField will return strs
#
#     status = forms.ChoiceField(
#         widget=forms.RadioSelect,
#         choices=STATUS_CHOICES,
#     )
