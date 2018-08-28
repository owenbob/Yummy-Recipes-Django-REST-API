from django.urls import path
from API.Users.views import UserAPIView


urlpatterns = [

    path('api/v1/register/', UserAPIView.as_view(), name="RegisterUsers"),
]