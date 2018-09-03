from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from API.serializers import RecipesSerializer
from django.contrib.auth.models import User
from API.models import (
    Categories,
    Recipes
)


class RecipesCreateAPIView(APIView):

    def post(self, request, category_id):
        exact_cat = Categories.objects.get(id=category_id)

        if exact_cat.user.id == request.user.id:
            data = {
                "recipe_title": request.data.get("recipe_title"),
                "recipe_description": request.data.get("recipe_description"),
                "category": exact_cat.id,
                "created_by_user": request.user.id
            }

            serializer = RecipesSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED)
            else:
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class RecipesListAPIView(APIView):

    def get(self, request):
        recipes_list = Recipes.objects.filter(created_by_user=request.user.id)
        data = RecipesSerializer(recipes_list, many=True).data
        return Response(data)


class RecipeRetrieveUpdateDelete(APIView):

    def get(self, request, recipe_id):
        try:
            retrieve_recipe = Recipes.objects.get(
                id=recipe_id,
                created_by_user=request.user.id)

            if retrieve_recipe:
                data = RecipesSerializer(retrieve_recipe, many=False).data
                return Response(data)
        except:
            error_message = "Category with id {} not found".format(recipe_id)
            return Response(error_message,status=status.HTTP_404_NOT_FOUND)

    def put(self, request, recipe_id):
        try:
            update_recipe = Recipes.objects.get(
                id=recipe_id,
                created_by_user=request.user.id
            )

            if update_recipe:
                try:
                    update_recipe.recipe_title = request.data.get("recipe_title")
                    update_recipe.recipe_description = request.data.get(
                        "recipe_description")
                    update_recipe.save()
                except BaseException:
                    error_message = "Ensure that you are updating both recipe_title and recipe_description"
                    return Response(
                        error_message,
                        status=status.HTTP_400_BAD_REQUEST)

                serializer = RecipesSerializer(update_recipe)
                if serializer.is_valid:
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(
                        serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

        except:
            error_message = "Category with id {} not found".format(recipe_id)
            return Response(error_message,status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, recipe_id):
        try:
            delete_recipe = Recipes.objects.get(
                id=recipe_id,
                created_by_user=request.user.id
            )
            if delete_recipe:
                delete_recipe.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        except:
            error_message = "Category with id {} not found".format(recipe_id)
            return Response(error_message,status=status.HTTP_404_NOT_FOUND)
