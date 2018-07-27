# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from character_sheets.forms import CharacterCreateForm
from character_sheets.models import Character, BasicFactsMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


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
            return redirect('characters_list')
    else:
        form = CharacterCreateForm()
        return render(request, 'character_sheets/character_create.html', {'form': form})


def characters_list(request):
    characters_list = Character.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(characters_list, 5)

    try:
        characters = paginator.page(page)
    except PageNotAnInteger:
        characters = paginator.page(1)
    except EmptyPage:
        characters = paginator.page(paginator.num_pages)

    return render(request, 'character_sheets/characters_list.html', {'characters': characters})


def character_detail(request, character_id):
    character = get_object_or_404(Character, pk=character_id)
    return render(request, 'character_sheets/character_detail.html', {'character': character})


def character_edit(request, character_id):
    character = get_object_or_404(Character, pk=character_id)
    return render(request, 'character_sheets/character_edit.html', {'character': character})