from django.urls import path

from API.Users.views import UserAPIView
from API.Category.views import (
    CategoriesCreateListAPIView,
    CategoriesRetrieveUpdateDestroyAPIView
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
    )
]