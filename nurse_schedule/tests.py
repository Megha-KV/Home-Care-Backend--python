from django.test import TestCase
from .models import NurseSchedule
from datetime import date, time

class NurseScheduleTestCase(TestCase):
    def setUp(self):
        # Create a sample instance of NurseSchedule for testing
        self.schedule = NurseSchedule.objects.create(
            nurse_id="N001",
            patient_name="John Doe",
            start_date=date(2024, 4, 25),
            end_date=date(2024, 4, 30),
            start_time=time(8, 0, 0),
            end_time=time(16, 0, 0),
            address="123 Main St",
            mr_no="MR123",
            role="Nurse",
            consult_id="CONS001",
        )

    def test_schedule_creation(self):
        # Test if a NurseSchedule instance is created correctly
        self.assertEqual(self.schedule.nurse_id, "N001")
        self.assertEqual(self.schedule.patient_name, "John Doe")
        self.assertEqual(self.schedule.start_date, date(2024, 4, 25))
        self.assertEqual(self.schedule.end_date, date(2024, 4, 30))
        self.assertEqual(self.schedule.start_time, time(8, 0, 0))
        self.assertEqual(self.schedule.end_time, time(16, 0, 0))
        self.assertEqual(self.schedule.address, "123 Main St")
        self.assertEqual(self.schedule.mr_no, "MR123")
        self.assertEqual(self.schedule.role, "Nurse")
        self.assertEqual(self.schedule.consult_id, "CONS001")

    # Add more test methods as needed to cover other functionalities of your model

    def tearDown(self):
        # Clean up any resources or data created during testing
        self.schedule.delete()