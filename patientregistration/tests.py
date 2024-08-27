from django.test import TestCase
from .models import Patientregistration

class PatientRegistrationTestCase(TestCase):
    def setUp(self):
        # Create a sample instance of Patientregistration for testing
        self.patient = Patientregistration.objects.create(
            File_no=12345,
            mr_no="MR123",
            consult_id="CONS001",
            dept="Cardiology",
            status="Active",
            date="2024-04-25",
            time="12:00:00",
            clinician="Dr. John Doe",
            ord_clinician="Dr. Jane Smith",
            ref_clinician="Dr. Michael Johnson",
            diag_clinic="Cardiology Clinic",
            diag_clinician="Dr. Sarah Brown",
            title="Mr",
            first_name="John",
            middle_name="William",
            last_name="Smith",
            dob="1990-01-01",
            age=34,
            sex="Male",
            marital_status="Single",
            nationality="American",
            emirated_id="E12345",
            religion="Christian",
            passport_id="P12345",
            unified="U12345",
            photo="photos/default.jpg",
            full_name="Jane Doe",
            relationship="Spouse",
            contact="1234567890",
            address="123 Main St",
            address1="Apt 101",
            address2="Building B",
            resi_of_emirates="Dubai",
            city="Dubai",
            contact_no="9876543210",
            work_no="9876543211",
            email="john@example.com",
            company="ABC Corporation",
            plan="Health Plan",
            membership_id="M12345",
            additional_info="Additional info here",
            issue_date="2023-01-01",
            expiry_date="2024-12-31",
            eligibility_id="EID123",
            payer_id="PID123",
        )

    def test_patient_creation(self):
        # Test if a patient instance is created correctly
        self.assertEqual(self.patient.File_no, 12345)
        self.assertEqual(self.patient.mr_no, "MR123")
        # Add more assertions to test other fields as needed

    # Add more test methods as needed to cover other functionalities of your model

    def tearDown(self):
        # Clean up any resources or data created during testing
        self.patient.delete()