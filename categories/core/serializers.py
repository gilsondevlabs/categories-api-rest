# -*- coding: utf-8 -*-

from rest_framework import serializers

from categories.core.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "children",)
