from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required

from character_sheets.forms import CharacterForm
from character_sheets.models import Character
from character_sheets.serializers import UserSerializer, CharacterSerializer


def character_list(request):
    characters = Character.objects.all()
    return render(request, 'character_sheets/character_list.html', {'characters': characters})


def sheets_base(request):
    return render(request, 'character_sheets/sheets_base.html', {})


@login_required
def character_create(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        form = CharacterForm(request.POST)
        if form.is_valid():
            character = form.save(commit=False)
            character.description = form.cleaned_data['description']
            character.character_class = form.cleaned_data['character_class']
            character.name = form.cleaned_data['name']
            character.creator = request.user
            character.created_date = timezone.now()
            character.save()
            return redirect('character_detail', pk=character.pk)
    else:
        form = CharacterForm()
    return render(request, 'character_sheets/character_edit.html', {'form': form})


@login_required
def character_edit(request, pk):
    character = get_object_or_404(Character, pk=pk)
    if request.method == "POST":
        form = CharacterForm(request.POST, instance=character)
        if form.is_valid():
            character = form.save(commit=False)
            character.description = form.cleaned_data['description']
            character.character_class = form.cleaned_data['character_class']
            character.name = form.cleaned_data['name']
            character.creator = request.user
            character.created_date = timezone.now()
            character.save()
            return redirect('character_detail', pk=character.pk)
    else:
        form = CharacterForm(instance=character)
    return render(request, 'character_sheets/character_edit.html', {'form': form})


@login_required
def character_detail(request, pk):
    character = Character.objects.get(pk=pk)
    return render(request, 'character_sheets/character_detail.html', {'character': character})


# ViewSets define the view behavior.
class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
