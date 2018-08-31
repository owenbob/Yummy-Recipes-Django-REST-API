from API.tests.base import BaseTestCase
from django.urls import reverse
from rest_framework import status

from API.models import Categories



class CategoryTestCase(BaseTestCase):

    def test_create_category(self):

        response = self.category_create_request
        
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(response.data["category_title"],self.category_data["category_title"])
        self.assertEqual(response.data["category_description"], self.category_data["category_description"])

    def test_list_category(self):

        category_to_list = self.category_create_request 

        self.client.credentials(HTTP_AUTHORIZATION=self.headers)

        response = self.client.get(
            reverse("CategoriesCreateList"),
            format='json'
        )
        
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(
            response.data[0]["category_title"],
            self.category_data["category_title"]
        )
        self.assertEqual(
            response.data[0]["category_description"],
            self.category_data["category_description"]
        )

    def test_retrieve_category(self):

        category_to_list = self.category_create_request 
        
        response = self.category_retrieve_request
        
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(
            response.data["category_title"],
            self.category_data["category_title"]
            )
        self.assertEqual(
            response.data["category_description"], 
            self.category_data["category_description"]
            )

    def test_update_category(self):

        category_to_update = self.category_create_request

        response = self.client.put(
            reverse(
                'CategoriesRetrieveUpdateDestroy',
                kwargs={'pk':Categories.objects.get(category_title='Test Title').id}
            ),
            self.category_update_data,
            HTTP_AUTHORIZATION=self.headers,
            format='json'
            )
        
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(
            response.data["category_title"],
            self.category_update_data["category_title"]
            )
        self.assertEqual(
            response.data["category_description"],
            self.category_update_data["category_description"]
            )
    
    def test_delete_category(self):

        category_to_delete = self.category_create_request

        response = self.client.delete(
           reverse(
                'CategoriesRetrieveUpdateDestroy',
                kwargs={'pk':Categories.objects.get(category_title='Test Title').id}
            ),
            HTTP_AUTHORIZATION=self.headers,
            format='json'
        )  
        

        import pdb; pdb.set_trace()
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
