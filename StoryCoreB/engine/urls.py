from django.urls import path
from . import views

urlpatterns = [
    # Stories
    path("stories/", views.stories),
    path("stories/<int:pk>/", views.story_detail),

    # Story -> Nodes
    path("stories/<int:pk>/nodes/", views.story_nodes),

    # Nodes
    path("nodes/<int:pk>/", views.node_detail),

    # Node -> Choices
    path("nodes/<int:pk>/choices/", views.node_choices),

    # Choices
    path("choices/<int:pk>/", views.choice_detail),
]