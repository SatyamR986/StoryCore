from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Story, Node
from .serializers import (
    StoryListSerializer,
    StoryDetailSerializer,
    StoryCreateSerializer,
    NodeDetailSerializer,
    NodeCreateSerializer,
    ChoiceSerializer
)


@api_view(["GET", "POST"])
def story_list_create(request):

    if request.method == "GET":
        stories = Story.objects.all()
        serializer = StoryListSerializer(stories, many=True)
        return Response(serializer.data)

    serializer = StoryCreateSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)


@api_view(["GET"])
def story_detail(request, pk):

    try:
        story = Story.objects.get(pk=pk)
    except Story.DoesNotExist:
        return Response(status=404)

    serializer = StoryDetailSerializer(story)
    return Response(serializer.data)


@api_view(["GET", "POST"])
def story_nodes_create(request, pk):

    try:
        story = Story.objects.get(pk=pk)
    except Story.DoesNotExist:
        return Response(status=404)


    if request.method == "GET":
        nodes = story.nodes.all()
        serializer = NodeDetailSerializer(nodes, many=True)
        return Response(serializer.data)


    serializer = NodeCreateSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(story=story)
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)


@api_view(["POST"])
def node_choices_create(request, pk):

    try:
        node = Node.objects.get(pk=pk)
    except Node.DoesNotExist:
        return Response(status=404)

    serializer = ChoiceSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(from_node=node)
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)