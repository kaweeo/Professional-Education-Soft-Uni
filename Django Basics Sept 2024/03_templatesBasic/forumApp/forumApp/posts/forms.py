from django import forms
from django.contrib.auth import authenticate
from django.forms import formset_factory
from forumApp.posts.mixins import DisableFieldsMixin
from django.core.exceptions import ValidationError
# from forumApp.posts.choices import LanguageChoice
from forumApp.posts.models import Post, Comment



class PostAuthorForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author',)


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

    def clean_author(self):  # This method will be call from full_clean (searches for 'clean_*')
        author = self.cleaned_data.get('author')

        if not author[0].isupper():
            raise ValidationError('Author name should start with capital letter!')

        return author

    def clean(self):  # Overriding the clean method to inplement custom logic between the fields
        cleaned_data = super().clean()

        title = cleaned_data.get('title')
        content = cleaned_data.get('content')

        if title and content and title in content:
            raise ValidationError('The post title should not be inclunded in content!')

        return cleaned_data

    def save(self, commit=True):  # Overriding the save method
        post = super().save(commit=False)  # Request for saving in the DB is not sent, only instance of a post

        post.title = post.title.capitalize()

        if commit:
            post.save()

        return post


class PostCreateForm(PostBaseForm):
    pass


class PostEditForm(PostBaseForm):
    pass


class PostDeleteForm(PostBaseForm, DisableFieldsMixin):
    # disabled_fields = ('title', 'author')
    disabled_fields = ('__all__',)


class SearchForm(forms.Form):
    query = forms.CharField(
        label="",
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Search for a post..."}),
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'content')

        labels = {
            'author': '',
            'content': '',
        }

        error_messages = {
            'author': {
                'required': "Please enter the author name!",
            },
            'content': {
                'required': "Contet is required!",
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['author'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your Name',
        })

        self.fields['content'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your Content...',
        })

CommentFormSet = formset_factory(CommentForm, extra=3)






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
