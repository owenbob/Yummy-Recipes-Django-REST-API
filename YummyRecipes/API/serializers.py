from rest_framework import serializers

from django.contrib.auth import get_user_model

from API.models import Categories



User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    categories = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Categories.objects.all())

    class Meta:
        model = User
        fields =("username","email","password","categories")