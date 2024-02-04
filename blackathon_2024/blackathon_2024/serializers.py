"""
serializer.py stores Serializer classes to translate Django models into json 
for usage in the frontend. Used in API calls in views.py.
"""
from rest_framework import serializers
from .models import Perspectives, Events