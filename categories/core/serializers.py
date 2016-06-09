# -*- coding: utf-8 -*-

from rest_framework import serializers

from rest_framework_recursive.fields import RecursiveField

from categories.core.models import Category


class CategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.ListSerializer(source="children",
                                               child=RecursiveField())

    class Meta:
        model = Category
        fields = ("id", "name", "subcategories",)
