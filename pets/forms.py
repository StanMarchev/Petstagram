from django import forms

from petstagram.pets.models import Pet


class PetAddForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'date_of_birth', 'personal_photo']
        # widgets = {
        #     'name' : forms.TextInput(
        #         attrs={
        #             'placeholder':'Pet name',
        #         }
        #     ),
        #     'date_of_birth':forms.DateInput(
        #         attrs={
        #             'placeholder':'mm/dd/yyyy',
        #             'type':'date'
        #         }
        #     ),
        #     'personal_photo': forms.URLField(
        #         attrs={
        #             'placeholder': 'Link to image',
        #         }
        #     )
        # }


class PetEditForm(forms.ModelForm):
    pass

class PetDeleteForm(forms.ModelForm):
    pass