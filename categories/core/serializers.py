# -*- coding: utf-8 -*-

from rest_framework import serializers

from categories.core.models import Category


class RecursiveField(serializers.Serializer):
    """
    Cria instancia do serializer parente e retorna os dados
    serializados.
    """
    def to_representation(self, value):
        ParentSerializer = self.parent.parent.__class__
        serializer = ParentSerializer(value, context=self.context)
        return serializer.data


class CategorySerializer(serializers.ModelSerializer):
    subcategories = RecursiveField(source="children", many=True)

    class Meta:
        model = Category
        fields = ("id", "name", "subcategories",)
