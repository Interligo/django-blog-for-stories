from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from api.serializers import StoryDetailSerializer
from api.serializers import StoriesListSerializer
from api.serializers import StoryDetailTextSerializer
from stories.models import Story


class StoryCreateView(generics.CreateAPIView):
    """Story creation for admins by API."""
    serializer_class = StoryDetailSerializer
    permission_classes = (IsAdminUser,)


class StoriesListView(generics.ListAPIView):
    """Stories list for all by API"""
    serializer_class = StoriesListSerializer
    queryset = Story.objects.all()


class StoryChangeView(generics.RetrieveUpdateDestroyAPIView):
    """Stories change for admins by API."""
    serializer_class = StoryDetailSerializer
    queryset = Story.objects.all()
    permission_classes = (IsAdminUser,)


class StoryDetailView(generics.RetrieveAPIView):
    """Story detail for all by API."""
    serializer_class = StoryDetailTextSerializer
    queryset = Story.objects.all()
