from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from character_sheets.forms import CharacterForm
from character_sheets.models import Character


def character_list(request):
    characters = Character.objects.all()
    return render(request, 'character_sheets/character_list.html', {'characters': characters})


def sheets_base(request):
    return render(request, 'character_sheets/sheets_base.html', {})


def character_create(request):
    # if this is a POST request we need to process the form data
    form = CharacterForm()
    return render(request, 'character_sheets/character_edit.html', {'form': form})


def character_detail(request, character_id):
    character = Character.objects.get(character_id=character_id)
    return render(request, 'character_sheets/character_detail.html', {'character': character})