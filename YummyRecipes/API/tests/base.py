
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.test import APIRequestFactory
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse

from API.models import Categories
from API.models import Recipes

# Define this after the ModelTestCase


class BaseTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.factory = APIRequestFactory()
        self.user_data = {
            "username": "Jacky123",
            "email": "jackychan123@gmail.com",
            "password": "123"
        }

        self.user_login_data = {
            "username" : "Jacky123",
            "password" : "123"
        }

        self.user_register_request = self.client.post(
            reverse('RegisterUsers'),
            self.user_data,
            format="json")

        self.user_login_request = self.client.post(
            reverse('Login'),
            self.user_login_data,
            format="json")

        token = self.user_login_request.data["token"]
        self.headers = "Token {}".format(token)

        self.category_data = {
            "category_title" : "Test Title",
            "category_description" : "Test Description"
        }

        self.category_update_data = {
            "category_title" : "Test Update Title",
            "category_description" : "Test Update Description"
        }

        self.category_create_request = self.client.post(
            reverse("CategoriesCreateList"),
            self.category_data,
            HTTP_AUTHORIZATION=self.headers,
            format='json'  
        )
        self.category_retrieve_request = self.client.get(
            reverse(
                'CategoriesRetrieveUpdateDestroy',
                kwargs={'pk':Categories.objects.get(category_title='Test Title').id}
            ),
            HTTP_AUTHORIZATION=self.headers,
            format='json'
            )
        
        self.recipe_data = {
            "recipe_title":"Rolex",
            "recipe_description":"Eggs"
            }
 
        self.recipe_create_request = self.client.post(
            reverse(
            'RecipesCreate',
            kwargs={'category_id':Categories.objects.get(category_title='Test Title').id}
            ),
            self.recipe_data,
            HTTP_AUTHORIZATION=self.headers,
            format='json'
        )

        self.recipe_update_data = {
            "recipe_title":"Test Update Recipes",
            "recipe_description":"Test Update Recipes"
            }
