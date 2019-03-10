from django import forms
from .models import Character


class CharacterForm(forms.ModelForm):
    # character_name = forms.CharField(label='Character Name', max_length=50)
    # class_choices = [
    #     ('BARBARIAN', 'Barbarian'),
    #     ('BARD', 'Bard'),
    #     ('CLERIC', 'Cleric'),
    #     ('DRUID', 'Druid'),
    #     ('FIGHTER', 'Fighter'),
    #     ('MONK', 'Monk'),
    #     ('PALADIN', 'Paladin'),
    #     ('RANGER', 'Ranger'),
    #     ('ROGUE', 'Rogue'),
    #     ('SORCEROR', 'Sorceror'),
    #     ('WARLOCK', 'Warlock'),
    #     ('WIZARD', 'Wizard'),
    #     ('NO_CLASS', 'No Class'),
    # ]
    # character_class = forms.ChoiceField(choices=class_choices, label='Character Class')

    class Meta:
        model = Character
        fields = ('name', 'character_class',)
