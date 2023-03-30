from django.contrib import admin
from django.urls import path, include
from blog import urls as blog_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("", include(blog_urls)),
]
