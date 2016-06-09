# -*- coding: utf-8 -*-

from rest_framework import serializers

from rest_framework_recursive.fields import RecursiveField

from categories.core.models import Category


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    subcategories = serializers.ListSerializer(source="children",
                                               required=False,
                                               child=RecursiveField())

    class Meta:
        model = Category
        fields = ("id", "name", "subcategories",)

    def validate(self, data):
        name = data.get('name', None)
        subcategories = data.get('subcategories', None)

        if not name and not subcategories:
            raise serializers.ValidationError(
                "Insira subcategoria para associação."
            )
        return data
