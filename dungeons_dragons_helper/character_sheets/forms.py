from django import forms

from .models import Character


class CharacterCreateForm(forms.ModelForm):

    character_name = forms.CharField()

    class Meta:
        model = Character
        fields = ('character_name',)