from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Story, Node, Choice
from drf_spectacular.utils import extend_schema
from .serializers import (
    StoryListSerializer,
    StoryDetailSerializer,
    StoryCreateSerializer,
    NodeListSerializer,
    NodeDetailSerializer,
    NodeCreateSerializer,
    ChoiceSerializer
)

@extend_schema(tags=["Stories"])
@api_view(["GET", "POST"])
def stories(request):

    if request.method == "GET":
        stories = Story.objects.all()
        serializer = StoryListSerializer(stories, many=True)
        return Response(serializer.data)

    serializer = StoryCreateSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)


@extend_schema(tags=["Stories"])
@api_view(["GET", "PATCH", "DELETE"])
def story_detail(request, pk):

    try:
        story = Story.objects.get(pk=pk)
    except Story.DoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = StoryDetailSerializer(story)
        return Response(serializer.data)

    if request.method == "PATCH":
        serializer = StoryDetailSerializer(story, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    if request.method == "DELETE":
        story.delete()
        return Response(status=204)


@extend_schema(tags=["Nodes"])
@api_view(["GET", "POST"])
def story_nodes(request, pk):

    try:
        story = Story.objects.get(pk=pk)
    except Story.DoesNotExist:
        return Response(status=404)


    if request.method == "GET":
        nodes = story.nodes.all()
        serializer = NodeListSerializer(nodes, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = NodeCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(story=story)
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


@extend_schema(tags=["Nodes"])
@api_view(["GET", "PATCH", "DELETE"])
def node_detail(request, pk):

    try:
        node = Node.objects.get(pk=pk)
    except Node.DoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = NodeDetailSerializer(node)
        return Response(serializer.data)

    if request.method == "PATCH":
        serializer = NodeCreateSerializer(node, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    if request.method == "DELETE":
        node.delete()
        return Response(status=204)


@extend_schema(tags=["Choices"])
@api_view(["POST"])
def node_choices(request, pk):

    try:
        node = Node.objects.get(pk=pk)
    except Node.DoesNotExist:
        return Response(status=404)
    
    serializer = ChoiceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(from_node=node)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
    

@extend_schema(tags=["Choices"])
@api_view(["GET", "PATCH", "DELETE"])
def choice_detail(request, pk):    
    
    try:
        choice = Choice.objects.get(pk=pk)
    except Choice.DoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = ChoiceSerializer(choice)
        return Response(serializer.data)

    if request.method == "PATCH":
        serializer = ChoiceSerializer(choice, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    if request.method == "DELETE":
        choice.delete()
        return Response(status=204)
        