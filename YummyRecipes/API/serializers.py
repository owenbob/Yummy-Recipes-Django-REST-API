from rest_framework import serializers
from rest_framework.authtoken.models import Token

from django.contrib.auth import get_user_model

from API.models import (
    Categories,
    Recipes
    )



User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields =(
            "username", 
            "email", 
            "password",  
            )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
            )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user


class CategoriesSerializer(serializers.ModelSerializer): 
    user = serializers.PrimaryKeyRelatedField(
    read_only=True, 
    default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Categories
        fields = (
            "id", 
            "category_title", 
            "category_description", 
            "date_modified", 
            "user"
            )


class RecipesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = (
            "id",
            "recipe_title",
            "recipe_description",
            "date_modified"
        )
    