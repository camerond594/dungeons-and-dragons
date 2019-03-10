from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from character_sheets.forms import CharacterForm


def character_list(request):
    return render(request, 'character_sheets/character_list.html', {})


def character_create(request):
    # if this is a POST request we need to process the form data
    form = CharacterForm()
    return render(request, 'character_sheets/character_edit.html', {'form': form})


def character_detail(request):
    return render(request, 'character_sheets/character_list.html', {})