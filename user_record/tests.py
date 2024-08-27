from django.test import TestCase
from django.contrib.auth.hashers import check_password
from .models import appuser

class AppUserTestCase(TestCase):
    def setUp(self):
        # Create a sample instance of appuser for testing
        self.user = appuser.objects.create(
            first_name="John",
            middle_name="Doe",
            last_name="Smith",
            job="Doctor",
            role="Admin",
            type_mode="Type",
            license="123456",
            validity="2024-12-31",
            user_id="john123",
            password="testpassword",
            cs_allow="Yes",
            session_exp="2024-04-30",
            email="john@example.com",
            mf_no="MF123",
            creation_date="2024-04-25",
            photo="photos/default.jpg",
            otp=None,
            is_superuser=False,
            is_staff=False,
            is_active=True,
        )

    def test_set_password(self):
        # Test if set_password method correctly hashes the password
        raw_password = "testpassword"
        self.user.set_password(raw_password)
        self.assertTrue(check_password(raw_password, self.user.password))

    def test_user_authentication(self):
        # Test the is_authenticated property
        self.assertTrue(self.user.is_authenticated)

    def test_user_anonymity(self):
        # Test the is_anonymous property
        self.assertFalse(self.user.is_anonymous)

    # Add more test methods as needed to cover other functionalities of your model

    def tearDown(self):
        # Clean up any resources or data created during testing
        self.user.delete()