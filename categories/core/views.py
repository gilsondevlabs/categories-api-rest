# -*- coding: utf-8 -*-

from rest_framework import generics

from categories.core.serializers import CategorySerializer
from categories.core.models import Category


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
