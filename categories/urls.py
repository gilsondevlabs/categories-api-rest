# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib import admin

from categories.core.views import CategoryView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^categories/', CategoryView.as_view()),
]
