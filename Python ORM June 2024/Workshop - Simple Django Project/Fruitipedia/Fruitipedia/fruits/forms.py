from django import forms
from .models import Category, Fruit


# # Base Forms in Django
# class CategoryForm(forms.ModelForm):
#     name = forms.CharField(
#         name=forms.CharField(
#             max_length=100,
#             required=True,
#         ),
#
#         widget=forms.TextInput(
#             attrs={'class': 'form-control'}
#         )
#     )


class CategoryBaseForm(forms.ModelForm):
    class Meta:
        model = Category
        # fields = ['name']
        fields = '__all__'


class CategoryAddForm(CategoryBaseForm):
    pass


class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit name', }),
            'description': forms.TextInput(attrs={'placeholder': 'Enter the description', }),
            'image_url': forms.URLInput(attrs={'placeholder': 'Enter the image url', }),
            'nutrition': forms.NumberInput(attrs={'placeholder': 'Enter the fruit nutrition', }),
        }

class FruitAddForm(FruitBaseForm):
    pass


class EditFruitForm(FruitBaseForm):
    pass


class DeleteFruitForm(FruitBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True
