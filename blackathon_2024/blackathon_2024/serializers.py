"""
serializer.py stores Serializer classes to translate Django models into json 
for usage in the frontend. Used in API calls in views.py.
"""
from rest_framework import serializers
from .models import Tags, Perspectives, Events


class TagsSerializer(serializers.ModelSerializer):
    """
    Serializer for a Tags model.

    Args:
        serializers (Serializer): generic serializer
    """

    class Meta:
        db_table = 'tags'
        model = Tags
        fields = '__all__'


class PerspectivesSerializer(serializers.ModelSerializer):
    """
    Serializer for a Perspectives model.

    Args:
        serializers (Serializer): generic serializer
    """

    class Meta:
        db_table = 'perspectives'
        model = Perspectives
        fields = '__all__'

class EventsSerializer(serializers.ModelSerializer):
    """
    Serializer for a Events model.

    Args:
        serializers (Serializer): generic serializer
    """

    class Meta:
        db_table = 'events'
        model = Events
        fields = '__all__'