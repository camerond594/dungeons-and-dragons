from django.test import TestCase
from character_sheets.models import Character


class SheetTestCase(TestCase):

    def setUp(self):
        pass

    def test_can_create_character(self):
        character_data = {
            'name': 'Test Character',
            'description': 'Just a test character',
            'character_class': 'BARB',
        }
        pass

        # response = self.client.post("/api/v1/register/", {
        #   "name": "Walter",
        #   "lasT_name": "White",
        #   "email": "heisenberg@email.com",
        #   "password": "secret", })