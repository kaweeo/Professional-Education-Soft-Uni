from django import forms

class PersonForm(forms.Form):
    STATUS_CHOICES = (
        (1, 'Draft'),
        (2, 'Published'),
        (3, 'Archived'),
    )

    person_name = forms.CharField(
        # widget=forms.TextInput(
        #     attrs={'class': 'form-control'}
        # )
    )

    age = forms.IntegerField()

    is_lecturer = forms.BooleanField()

    status = forms.IntegerField(
        widget=forms.Select(choices=STATUS_CHOICES)
    )       # IntegerField + widget returns ints, ChoiceField will return strs

    # status = forms.ChoiceField(
    #     choices=STATUS_CHOICES,
    # )