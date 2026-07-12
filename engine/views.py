from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Story, Node, Choice
from .serializers import StorySerializer, NodeSerializer


@api_view(["GET"])
def story_list(request):

    stories = Story.objects.all()

    serializer = StorySerializer(
        stories,
        many=True
    )

    return Response(serializer.data)

@api_view(["POST"])
def story_create(request):
    serializer = StorySerializer(data=request.data)
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

    serializer = StorySerializer(story)
    return Response(serializer.data)

@api_view(["GET"])
def node_detail(request, pk):
    try:
        node = Node.objects.get(pk=pk)
    except Node.DoesNotExist:
        return Response(status=404)

    serializer = NodeSerializer(node)
    return Response(serializer.data)