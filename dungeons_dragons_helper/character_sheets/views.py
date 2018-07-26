# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from character_sheets.forms import CharacterCreateForm
from character_sheets.models import Character, BasicFactsMixin


def create_character(request):
    if request.method == "POST":
        form = CharacterCreateForm(request.POST)
        if form.is_valid():
            character = form.save(commit=False)
            character.active = True
            facts = BasicFactsMixin()
            facts.character_name = form.cleaned_data['character_name']
            facts.character_class = None
            facts.character_level = 1
            facts.character_race = None
            facts.character_background = None
            facts.character_alignment = None
            facts.character_exp_points = 0
            facts.save()
            character.facts = facts
            character.save()
            return redirect('get_characters')
    else:
        form = CharacterCreateForm()
        return render(request, 'character_sheets/create_character.html', {'form': form})


# This method is a stub — Finish later
def list_edit_characters(request):
    characters = Character.objects.all()
    return render(request, 'character_sheets/list_edit_characters.html', {'characters': characters})


# This method is a stub — Finish later
def get_characters(request):
    characters = Character.objects.all()
    return render(request, 'character_sheets/view_characters.html', {'characters': characters})
