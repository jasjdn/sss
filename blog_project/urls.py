from django.contrib import admin
from django.urls import path, include  # new
# from . import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),  # new
    # path("ay/", views.ay),



]
