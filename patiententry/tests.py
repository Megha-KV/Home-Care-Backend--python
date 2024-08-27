from django.test import TestCase
from .models import Entry

class EntryTestCase(TestCase):
    def setUp(self):
        # Create a sample instance of Entry for testing
        self.entry = Entry.objects.create(
            nurse_note="Test nurse note",
            nurse_name="Test Nurse",
        )

    def test_entry_creation(self):
        # Test if an Entry instance is created correctly
        self.assertEqual(self.entry.nurse_note, "Test nurse note")
        self.assertEqual(self.entry.nurse_name, "Test Nurse")
        # Add more assertions to test other fields as needed

    # Add more test methods as needed to cover other functionalities of your model

    def tearDown(self):
        # Clean up any resources or data created during testing
        self.entry.delete()