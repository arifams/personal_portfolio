from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("projects/", include("projects.urls")),
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path("blog/", include("blog.urls")),
]