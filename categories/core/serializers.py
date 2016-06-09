# -*- coding: utf-8 -*-

from django.core.exceptions import ObjectDoesNotExist

from rest_framework import serializers

from categories.core.models import Category


class RecursiveField(serializers.BaseSerializer):
    """
    Cria instancia do serializer parente e retorna os dados
    serializados.
    """
    def to_representation(self, value):
        ParentSerializer = self.parent.parent.__class__
        serializer = ParentSerializer(value, context=self.context)
        return serializer.data

    def to_internal_value(self, data):
        ParentSerializer = self.parent.parent.__class__
        Model = ParentSerializer.Meta.model
        try:
            instance = Model.objects.get(pk=data)
        except ObjectDoesNotExist:
            raise serializers.ValidationError(
                "Objeto {0} não encontrado".format(
                    Model().__class__.__name__
                )
            )
        return instance


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    subcategories = RecursiveField(source="children",
                                   many=True, required=False)

    class Meta:
        model = Category
        fields = ("id", "name", "subcategories",)

    def validate(self, data):
        name = data.get('name', None)
        subcategories = data.get('children', None)

        if not name and not subcategories:
            raise serializers.ValidationError("Insira subcategoria para associação.")
        return data
