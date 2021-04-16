from rest_framework import serializers

from stories.models import Story


class StoryDetailSerializer(serializers.ModelSerializer):
    """Class for story creating and changing."""
    class Meta:
        model = Story
        fields = '__all__'


class StoriesListSerializer(serializers.ModelSerializer):
    """Class for stories list include only id (for detailing), title and winning place (for Interligo's priding)."""
    class Meta:
        model = Story
        fields = '__all__'


class StoryDetailTextSerializer(serializers.ModelSerializer):
    """Class for story detailing with text."""
    class Meta:
        model = Story
        fields = ('id', 'story_title', 'story_text')
