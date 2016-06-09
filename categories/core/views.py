# -*- coding: utf-8 -*-

from rest_framework import generics

from categories.core.serializers import CategorySerializer
from categories.core.models import Category


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.root_nodes()
    serializer_class = CategorySerializer
