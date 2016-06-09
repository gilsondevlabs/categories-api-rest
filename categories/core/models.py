# -*- coding: utf-8 -*-

from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=80, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='children', db_index=True)

    class MPTTMeta:
        db_table = "categories"
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
