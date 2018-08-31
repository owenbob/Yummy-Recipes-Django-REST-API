from django.contrib.auth import authenticate
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginView(APIView):
    permission_classes = ()
    def post(self, request,):
        username = request.data.get("username")
        raw_password = request.data.get("password")
        user = authenticate(username=username, password=raw_password)
        
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response(
                {"error": "Wrong Credentials"}, 
                status=status.HTTP_400_BAD_REQUEST
                )