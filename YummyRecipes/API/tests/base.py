
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User

# Define this after the ModelTestCase
class BaseTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.user_data = {
            "username":"Jacky123",
            "email":"jackychan123@gmail.com",
            "password":"123",
            "categories":[]
        }
        