from API.tests.base import BaseTestCase
from  rest_framework import status
from django.urls import reverse

from API.models import Categories

class RecipesTestCase(BaseTestCase):
    def test_create_recipes(self):
        response_cat = self.category_create_request

        response = self.recipe_create_request

        self.assertEquals(response.status_code,status.HTTP_201_CREATED)
        self.assertEquals(
            response.data.get("recipe_title"),
            self.recipe_data["recipe_title"]
        )
        self.assertEquals(
            response.data.get("recipe_description"),
            self.recipe_data["recipe_description"]
        )

    def test_list_recipe(self):

        response = self.recipe_create_request

        response = self.client.get(
            reverse("RecipesList"),
            HTTP_AUTHORIZATION=self.headers,
            format='json'
        )

        self.assertEquals(response.status_code,status.HTTP_200_OK)
        self.assertEquals(
            response.data[0]["recipe_title"],
            self.recipe_data["recipe_title"]
        )
        self.assertEquals(
            response.data[0]["recipe_description"],
            self.recipe_data["recipe_description"]
        )

    def test_retrieve_recipe(self):
        response_rec = self.recipe_create_request
        response = self.client.get(
            reverse(
                "RecipeRetrieveUpdateDelete",
                kwargs={
                    "recipe_id":response_rec.data.get("id")
                }
            ),
            HTTP_AUTHORIZATION=self.headers,
            format='json'
        )

        self.assertEquals(response.status_code,status.HTTP_200_OK)
        self.assertEquals(
            response.data.get("recipe_title"),
            self.recipe_data["recipe_title"]
        )
        self.assertEquals(
            response.data.get("recipe_description"),
            self.recipe_data["recipe_description"]
        )
    
    def test_update_recipe(self):
        response_rec = self.recipe_create_request
        response = self.client.put(
            reverse(
                "RecipeRetrieveUpdateDelete",
                kwargs={
                    "recipe_id":response_rec.data.get("id")
                }
            ),
            self.recipe_update_data,
            HTTP_AUTHORIZATION=self.headers,
            format='json'
        )

        self.assertEquals(response.status_code,status.HTTP_200_OK)
        self.assertEquals(
            response.data.get("recipe_title"),
            self.recipe_update_data["recipe_title"]
        )
        self.assertEquals(
            response.data.get("recipe_description"),
            self.recipe_update_data["recipe_description"]
        )
    
    def test_delete_recipe(self):

        response_rec = self.recipe_create_request
        response = self.client.delete(
            reverse(
                "RecipeRetrieveUpdateDelete",
                kwargs={
                    "recipe_id":response_rec.data.get("id")
                }
            ),
            self.recipe_update_data,
            HTTP_AUTHORIZATION=self.headers,
            format='json'
        )

        self.assertEquals(response.status_code,
            status.HTTP_204_NO_CONTENT)





        



