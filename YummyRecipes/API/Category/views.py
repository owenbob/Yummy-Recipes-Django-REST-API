from rest_framework import generics,mixins
from rest_framework.response import Response

from API.models import Categories
from API.serializers import CategoriesSerializer
from API.Category.mixins import (
    MyListModelMixin,
    MyRetrieveModelMixin,
    MyUpdateModelMixin,
    MyDestroyModelMixin
)


class CategoriesCreateListAPIView(
    generics.GenericAPIView,
    MyListModelMixin,
    mixins.CreateModelMixin,
):

    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CategoriesRetrieveUpdateDestroyAPIView(
    MyRetrieveModelMixin,
    MyUpdateModelMixin,
    MyDestroyModelMixin,
    generics.GenericAPIView
):

    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)