from django.urls import path
from . import views

urlpatterns = [
    path("stories/", views.story_list),
    path("stories/create/", views.story_create),
    path("stories/<int:pk>/", views.story_detail),
    path("stories/<int:pk>/nodes/", views.story_nodes),
]