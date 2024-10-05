from django import forms

class PersonForm(forms.Form):
    person_name = forms.CharField(
        # widget=forms.TextInput(
        #     attrs={'class': 'form-control'}
        # )
    )
    age = forms.IntegerField()
