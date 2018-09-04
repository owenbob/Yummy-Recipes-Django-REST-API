from rest_framework import status

from API.tests.base import BaseTestCase


class LoginTestCase(BaseTestCase):
    def test_user_login(self):
        
        response = self.user_login_request

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token",response.data)
