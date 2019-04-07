from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils import timezone

from character_sheets.forms import CharacterForm
from character_sheets.models import Character


def character_list(request):
    characters = Character.objects.all()
    return render(request, 'character_sheets/character_list.html', {'characters': characters})


def sheets_base(request):
    return render(request, 'character_sheets/sheets_base.html', {})


def character_create(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        form = CharacterForm(request.POST)
        if form.is_valid():
            character = form.save(commit=False)
            character.creator = request.user
            character.created_date = timezone.now()
            character.save()
            return redirect('character_detail', pk=character.pk)
    else:
        form = CharacterForm()
    return render(request, 'character_sheets/character_edit.html', {'form': form})


def character_detail(request, pk):
    character = Character.objects.get(pk=pk)
    return render(request, 'character_sheets/character_detail.html', {'character': character})