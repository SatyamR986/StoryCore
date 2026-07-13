from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from engine.models import Story, Node, Choice
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Play"])
@api_view(['GET'])
def play_story(request, story_id):

    try:
        story = Story.objects.get(pk=story_id)
    except Story.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = NodeSerializer(story.starting_node)
    return Response(serializer.data)


@extend_schema(tags=["Play"])
@api_view(['GET'])
def play_choice(request, choice_id):

    try:
        choice = Choice.objects.get(pk=choice_id)
    except Choice.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = NodeSerializer(choice.to_node)
    return Response(serializer.data)