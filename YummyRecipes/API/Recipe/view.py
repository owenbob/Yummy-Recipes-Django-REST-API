from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from API.serializers import RecipesSerializer
from django.contrib.auth.models import User
from API.models import Categories


class RecipesCreateAPIView(APIView):

    def post(self, request,category_id):
            exact_cat = Categories.objects.get(id=category_id)
        
            if exact_cat.user.id == request.user.id :
                data = {
                    "recipe_title":request.data.get("recipe_title"),
                    "recipe_description":request.data.get("recipe_description"),
                    "category":exact_cat.id
                }

                serializer = RecipesSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data,status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
