from API.tests.base import BaseTestCase
from django.urls import reverse
from rest_framework import status


class RegisterTestCase(BaseTestCase):
    def test_user_registration(self):

        response = self.user_register_request

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['email'], self.user_data['email'])
        self.assertEqual(response.data['username'], self.user_data['username'])
