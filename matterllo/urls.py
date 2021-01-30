# -*- coding: utf-8 -*-
from django.urls import path
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth import login, logout

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
]
