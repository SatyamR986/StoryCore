from rest_framework import serializers
from engine.models import Story, Node, Choice

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ("id", "text")

class NodeSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Node
        fields = ("id", "title", "text", "choices" )