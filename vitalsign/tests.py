from django.test import TestCase
from .models import PatientVitalSign

class PatientVitalSignTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.patient_vital_sign = PatientVitalSign.objects.create(
            cid="123456",
            mrn="7890",
            height="180",
            weight="70",
            bmi="21.6",
            rbs="120",
            fbs="100",
            o2_saturation="98",
            head_circum="55",
            chest_circum="90",
            waist_circum="80",
            hip_circum="95",
            abdo_circum="85",
            pain_score="5",
            temp_note="Normal",
            temp_site="Oral",
            pulse_note="Regular",
            pulse_site="Radial",
            respiration="16",
            bp_note="Normal",
            bp_site="Brachial"
        )

    def test_patient_vital_sign_creation(self):
        self.assertTrue(isinstance(self.patient_vital_sign, PatientVitalSign))
        self.assertEqual(str(self.patient_vital_sign), self.patient_vital_sign.cid)

    def test_patient_vital_sign_fields(self):
        vital_sign = PatientVitalSign.objects.get(cid="123456")
        self.assertEqual(vital_sign.mrn, "7890")
        self.assertEqual(vital_sign.height, "180")
        self.assertEqual(vital_sign.weight, "70")
        self.assertEqual(vital_sign.bmi, "21.6")
        self.assertEqual(vital_sign.rbs, "120")
        self.assertEqual(vital_sign.fbs, "100")
        self.assertEqual(vital_sign.o2_saturation, "98")
        self.assertEqual(vital_sign.head_circum, "55")
        self.assertEqual(vital_sign.chest_circum, "90")
        self.assertEqual(vital_sign.waist_circum, "80")
        self.assertEqual(vital_sign.hip_circum, "95")
        self.assertEqual(vital_sign.abdo_circum, "85")
        self.assertEqual(vital_sign.pain_score, "5")
        self.assertEqual(vital_sign.temp_note, "Normal")
        self.assertEqual(vital_sign.temp_site, "Oral")
        self.assertEqual(vital_sign.pulse_note, "Regular")
        self.assertEqual(vital_sign.pulse_site, "Radial")
        self.assertEqual(vital_sign.respiration, "16")
        self.assertEqual(vital_sign.bp_note, "Normal")
        self.assertEqual(vital_sign.bp_site, "Brachial")

    def test_created_time_auto_now(self):
        vital_sign = PatientVitalSign.objects.get(cid="123456")
        self.assertIsNotNone(vital_sign.created_time)
