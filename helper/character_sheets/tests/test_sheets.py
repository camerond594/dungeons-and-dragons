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
        }
        self.user = User.objects.create_superuser(username=test_user['username'], email='test@test.ca', password=test_user['password'])
        login = self.client.login(username='testuser', password='12345')
        pass

    def test_can_create_character(self):
        test_user = mommy.make(User)
        character_data = {
            'name': 'Test Character',
            'description': 'Just a test character',
            'character_class': 'BARB',
            'creator': 'http://localhost:8000/api/users/1/',
        }

        url = 'http://127.0.0.1:8000/api/characters/'

        factory = APIRequestFactory()
        request = self.client.post(path=url, data=json.dumps(character_data, indent=4, sort_keys=True, default=str), content_type='application/json')


        characters = Character.objects.all()
        character = Character.objects.first()

        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Character.objects.count(), 1)
        self.assertEqual(character.name, character_data['name'])