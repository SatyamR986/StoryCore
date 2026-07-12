from django.urls import path
from . import views

urlpatterns = [
    path("stories/", views.story_list_create),
    path("stories/<int:pk>/", views.story_detail),
    path("stories/<int:pk>/nodes/", views.story_nodes_create),
    path("nodes/<int:pk>/choices/", views.node_choices_create),
]