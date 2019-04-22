from django.contrib.auth.models import User
from django.forms import model_to_dict
from model_mommy import mommy
from rest_framework import status
from rest_framework.test import APITestCase, APIClient, APIRequestFactory, force_authenticate
from rest_framework.utils import json

from character_sheets.models import Character



class SheetTestCase(APITestCase):

    def setUp(self):
        test_user = {
            'username': 'testuser',
            'password': '12345',
            'email': 'test@test.ca',
        }
        self.user = User.objects.create_superuser(username=test_user['username'], email=test_user['email'], password=test_user['password'])
        login = self.client.login(username='testuser', password='12345')

    def test_can_create_character(self):
        character_data = {
            'name': 'Test Character',
            'description': 'Just a test character',
            'character_class': 'BARB',
            'creator': 'http://localhost:8000/api/users/1/',
        }

        url = 'http://127.0.0.1:8000/api/characters/'
        user_url = 'http://localhost:8000/api/users/' + str(self.user.id) + '/'

        request = self.client.post(path=url, data=json.dumps(character_data, indent=4, sort_keys=True, default=str), content_type='application/json')

        character = Character.objects.first()

        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Character.objects.count(), 1)
        self.assertEqual(character.name, character_data['name'])
        self.assertEqual(character.description, character_data['description'])
        self.assertEqual(character.character_class, character_data['character_class'])
        self.assertEqual(user_url, character_data['creator'])