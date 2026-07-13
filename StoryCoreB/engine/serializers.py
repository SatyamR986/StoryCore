from rest_framework import serializers
from .models import Story, Node, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = "__all__"

class NodeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = ("id", "title", "text")

class NodeDetailSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Node
        fields = ("id", "story", "title", "text", "choices")

class NodeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = ("title", "text")

class StoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ("id", "title", "description")

class StoryDetailSerializer(serializers.ModelSerializer):
    nodes = NodeDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Story
        fields = ("id", "title", "description", "created_at", "updated_at", "nodes")

class StoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ("title", "description")

