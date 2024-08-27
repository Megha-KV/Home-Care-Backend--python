from django.test import TestCase
from .models import ApieNote
from datetime import datetime

class ApieNoteTestCase(TestCase):
    def setUp(self):
        # Create a sample instance of ApieNote for testing
        self.note = ApieNote.objects.create(
            nurse_name="Test Nurse",
            assessment="Test assessment",
            planning="Test planning",
            intervention="Test intervention",
            evaluation="Test evaluation"
        )

    def test_note_creation(self):
        # Test if an ApieNote instance is created correctly
        self.assertIsInstance(self.note.date, datetime)
        self.assertEqual(self.note.nurse_name, "Test Nurse")
        self.assertEqual(self.note.assessment, "Test assessment")
        self.assertEqual(self.note.planning, "Test planning")
        self.assertEqual(self.note.intervention, "Test intervention")
        self.assertEqual(self.note.evaluation, "Test evaluation")

    # Add more test methods as needed to cover other functionalities of your model

    def tearDown(self):
        # Clean up any resources or data created during testing
        self.note.delete()