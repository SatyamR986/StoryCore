from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('gameplay/stories/<int:story_id>/play/', views.play_story),
    path('gameplay/choices/<int:choice_id>/play/', views.play_choice),
]