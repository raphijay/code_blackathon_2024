import json
from django.test import TestCase
from datetime import date, time
from django.urls import reverse
from rest_framework import status
from .models import Tags, Perspectives, Events
from .views import *

class ModelsTestCase(TestCase):

    def setUp(self):
        # Create a Tag
        self.tag = Tags.objects.create(title="Test Tag")

        # Create a Perspectives instance
        self.perspective = Perspectives.objects.create(
            title="Test Perspective",
            description="Test Description",
            upboat=10,
            downboat=5,
            year=2023
        )
        self.perspective.tags.add(self.tag)

        # Create an Events instance
        self.event = Events.objects.create(
            title="Test Event",
            date=date(2024, 2, 4),
            time=time(12, 30),
            description="Test Event Description"
        )
        self.event.tags.add(self.tag)

    def test_tag_str_representation(self):
        self.assertEqual(str(self.tag), "Test Tag")

    def test_perspectives_str_representation(self):
        self.assertEqual(str(self.perspective), "Test Perspective")

    def test_events_str_representation(self):
        self.assertEqual(str(self.event), "Test Event")

    def test_perspectives_tags_relationship(self):
        self.assertEqual(self.perspective.tags.count(), 1)
        self.assertEqual(self.perspective.tags.first(), self.tag)

    def test_events_tags_relationship(self):
        self.assertEqual(self.event.tags.count(), 1)
        self.assertEqual(self.event.tags.first(), self.tag)

    def test_events_date_default_value(self):
        today = date.today()
        self.assertEqual(self.event.date, today)

    def test_events_time_default_value(self):
        self.assertEqual(self.event.time, time(12, 30))

class ViewTestCase(TestCase):

    def test_endorse_valid(self):
        # Assumes theres a perspective with id #1
        response = self.client.post('http://127.0.0.1:8000/Perspective/1/Endorse/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_endorse_invalid_pk(self):
        response = self.client.post('http://127.0.0.1:8000/Perspective/400/Endorse/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_oppose_valid(self):
        response = self.client.post('http://127.0.0.1:8000/Perspective/1/Oppose/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_oppose_invalid_pk(self):
        response = self.client.post('http://127.0.0.1:8000/Perspective/400/Oppose/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_add_perspective(self):
        perspective_data = {
            "title": "why plantains are the best",
            "description": "they just are",
            "upboat": 621,
            "downboat": 0,
            "year": "1998",
        }
        response = self.client.post('http://127.0.0.1:8000/Perspective/', data=json.dumps(perspective_data), content_type='application/json')#, content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
