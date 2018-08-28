from django.shortcuts import render
from rest_framework.generics import CreateAPIView

# Create your views here.

from API.serializers import UserSerializer
from django.contrib.auth import get_user_model


User = get_user_model()


class UserAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new ."""
        serializer.save()


