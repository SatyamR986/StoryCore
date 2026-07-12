from rest_framework import serializers
from .models import Story, Node

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'  

class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = '__all__'
