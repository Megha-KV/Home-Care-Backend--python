from django.test import TestCase
from .models import GeneralDetails

class GeneralDetailsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.general_details = GeneralDetails.objects.create(
            op_no=123,
            first_name="John",
            age="30",
            sex="Male",
            full_name="John Doe",
            ref_clinician="Dr. Smith",
            privacy_mode="Private",
            general_appearance="Normal",
            vital_signs="Stable",
            other_signs="None",
            ears_examination="Normal",
            nose_examination="Normal",
            throat_examination="Normal",
            face_examination="Normal",
            neck_examination="Normal"
        )

    def test_general_details_creation(self):
        self.assertTrue(isinstance(self.general_details, GeneralDetails))
        self.assertEqual(str(self.general_details), str(self.general_details.op_no))

    def test_general_details_fields(self):
        details = GeneralDetails.objects.get(op_no=123)
        self.assertEqual(details.first_name, "John")
        self.assertEqual(details.age, "30")
        self.assertEqual(details.sex, "Male")
        self.assertEqual(details.full_name, "John Doe")
        self.assertEqual(details.ref_clinician, "Dr. Smith")
        self.assertEqual(details.privacy_mode, "Private")
        self.assertEqual(details.general_appearance, "Normal")
        self.assertEqual(details.vital_signs, "Stable")
        self.assertEqual(details.other_signs, "None")
        self.assertEqual(details.ears_examination, "Normal")
        self.assertEqual(details.nose_examination, "Normal")
        self.assertEqual(details.throat_examination, "Normal")
        self.assertEqual(details.face_examination, "Normal")
        self.assertEqual(details.neck_examination, "Normal")

    # Add more tests as needed for any custom methods or behaviors in your model
