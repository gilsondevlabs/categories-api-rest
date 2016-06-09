# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib import admin

from categories.core.views import CategoryView, CategoryDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^categories/(?P<pk>[0-9]+)$', CategoryDetailView.as_view()),
    url(r'^categories/', CategoryView.as_view()),
]
