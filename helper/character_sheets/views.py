from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils import timezone
from rest_framework import viewsets

from character_sheets.forms import CharacterForm
from character_sheets.models import Character
from character_sheets.serializers import UserSerializer, CharacterSerializer


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
