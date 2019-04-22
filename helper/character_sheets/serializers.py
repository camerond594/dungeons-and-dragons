from django.contrib.auth.models import User
from rest_framework import serializers

from character_sheets.models import Character


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        fields = ('name', 'description', 'creator', 'created_date', 'creator_id')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')