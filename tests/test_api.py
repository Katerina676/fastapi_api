from unittest import TestCase
from fastapi.testclient import TestClient

from app.main import application as web_app


class APITestCase(TestCase):

    def setUp(self):
        self.client = TestClient(web_app)

    def test_main_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)
        body = response.json()
        self.assertEqual(body, {'detail': 'Not Found'})

    def test_create_user(self):
        user_data = {
            'user': {
                'email': 'test122332@mail.com',
                'password': '123',
                'first_name': 'Kate',
                'last_name': 'Lost',
                'login': 'lalaland'
            }
        }

        response = self.client.post('/user', json=user_data)
        self.assertEqual(response.status_code, 200)
