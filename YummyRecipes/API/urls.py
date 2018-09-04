from django.urls import path

from API.Users.views import UserAPIView
from API.Category.views import (
    CategoriesCreateListAPIView,
    CategoriesRetrieveUpdateDestroyAPIView
)

from API.Recipe.view import (
    RecipesCreateAPIView,
    RecipesListAPIView,
    RecipeRetrieveUpdateDelete
    
)
from API.Auth.views import LoginView



urlpatterns = [

    path(
        'api/v1/register/', 
        UserAPIView.as_view(), 
        name="RegisterUsers"
    ),
    path(
        'api/v1/login',
        LoginView.as_view(),
        name='Login'
    ),
    path(
        'api/v1/auth/categories/', 
        CategoriesCreateListAPIView.as_view(), 
        name='CategoriesCreateList'
    ),
    path(
        'api/v1/auth/categories/<int:pk>', 
        CategoriesRetrieveUpdateDestroyAPIView.as_view(), 
        name='CategoriesRetrieveUpdateDestroy'
    ),
    path(
        'api/v1/auth/recipes/<int:category_id>',
        RecipesCreateAPIView.as_view(),
        name='RecipesCreate'

    ),
    path(
        'api/v1/auth/recipes/',
        RecipesListAPIView.as_view(),
        name='RecipesList'
    ),
    path(
        'api/v1/auth/recipe/<int:recipe_id>',
        RecipeRetrieveUpdateDelete.as_view(),
        name='RecipeRetrieveUpdateDelete'
    )
]