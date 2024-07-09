# projects/urls.py

from django.urls import path
from projects import views


urlpatterns = [
    path("projects/<int:pk>/", views.project_detail, name="project_detail"),
    path("people/", views.person_list, name="person_list"),
    path("people/<int:pk>/", views.person_detail, name="person_detail"),
    path("projects/", views.project_index, name="project_index"),
    path("search/", views.search, name="search"),
]

