from rest_framework import serializers
from .models import Story, Node, Choice

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'  



class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'
        

class NodeSerializer(serializers.ModelSerializer):
    choices  = ChoiceSerializer(many=True, read_only=True)
    class Meta:
        model = Node
        fields = ('id', 'story', 'title', 'text', 'choices')  