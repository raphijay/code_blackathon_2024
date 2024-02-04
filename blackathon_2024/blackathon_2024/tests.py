from django.test import TestCase
from datetime import date, time
from .models import Tags, Perspectives, Events

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
